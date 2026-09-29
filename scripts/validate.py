#!/usr/bin/env python3
"""Check that every expert profile and every registry that lists it agree.

Usage (from anywhere):  python3 scripts/validate.py

Checks each `scientific-agents/<slug>/` profile, `catalog.json`, `README.md`,
`.claude-plugin/marketplace.json`, and the two copies of the
create-scientific-agent skill. Exits 1 if any error is found; warnings are
printed but do not fail the run. Standard library only, so it runs in CI as-is.
"""

import itertools
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "scientific-agents"

# Codex truncates project docs past `project_doc_max_bytes` (default 32 KiB).
MAX_BYTES = 32 * 1024

# Share of a profile's content lines found verbatim in another profile. Distinct
# profiles overlap by under 10%; copied bodies sit at 50-99%.
MAX_OVERLAP = 0.25

# Standard section headings from the skill's agents-md-template.md.
CANONICAL_HEADINGS = [
    "Mindset And First Principles",
    "How You Frame A Problem",
    "How You Work",
    "Tools, Instruments, And Software",
    "Data, Resources, And Literature",
    "Rigor And Critical Thinking",
    "Troubleshooting Playbook",
    "Communicating Results",
    "Standards, Units, Ethics, And Vocabulary",
    "Definition Of Done",
]

CATALOG_FIELDS = {
    "profession": str,
    "slug": str,
    "path": str,
    "work_mode": str,
    "summary": str,
    "created": str,
    "updated": str,
    "source_count": int,
}

SKILL_COPIES = [
    ROOT / ".agents/skills/create-scientific-agent",
    ROOT / ".claude/skills/create-scientific-agent",
]

errors = []
warnings = []


def error(where, msg):
    errors.append(f"{where}: {msg}")


def warn(where, msg):
    warnings.append(f"{where}: {msg}")


def heading_key(text):
    """Collapse punctuation, case, and '&' vs 'And' so spelling variants match."""
    words = re.sub(r"[^a-z ]", "", text.lower().replace("&", "and")).split()
    return " ".join(w for w in words if w != "and")


CANONICAL_BY_KEY = {heading_key(h): h for h in CANONICAL_HEADINGS}


def load_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        error(path.relative_to(ROOT), f"cannot load JSON ({exc})")
        return None


def check_catalog():
    data = load_json(ROOT / "catalog.json")
    if data is None:
        return {}
    entries = data.get("agents", [])
    catalog = {}
    for i, entry in enumerate(entries):
        where = f"catalog.json[{i}]"
        for field, kind in CATALOG_FIELDS.items():
            if not isinstance(entry.get(field), kind):
                error(where, f"missing or non-{kind.__name__} field '{field}'")
        slug = entry.get("slug", "")
        if slug in catalog:
            error(where, f"duplicate slug '{slug}'")
        catalog[slug] = entry
        if entry.get("path") != f"{slug}/AGENTS.md":
            error(where, f"path should be '{slug}/AGENTS.md'")
        for field in ("created", "updated"):
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(entry.get(field, ""))):
                error(where, f"'{field}' is not YYYY-MM-DD")
        if str(entry.get("updated", "")) < str(entry.get("created", "")):
            error(where, "'updated' is earlier than 'created'")
        if entry.get("source_count") == 0:
            warn(f"catalog.json:{slug}", "source_count is 0 (no recorded research)")
    slugs = [e.get("slug", "") for e in entries]
    if slugs != sorted(slugs):
        out_of_order = [b for a, b in zip(slugs, slugs[1:]) if a > b]
        error("catalog.json", f"entries not sorted by slug (first: {out_of_order[0]})")
    return catalog


def check_profile(slug, entry):
    folder = PROFILES / slug
    where = f"scientific-agents/{slug}"
    agents_md_path = folder / "AGENTS.md"
    if not agents_md_path.is_file():
        error(where, "missing AGENTS.md")
        return None
    body = agents_md_path.read_text()
    summary = entry.get("summary", "")

    size = len(body.encode())
    if size > MAX_BYTES:
        error(f"{where}/AGENTS.md", f"{size} bytes exceeds the {MAX_BYTES}-byte Codex default")

    title = body.split("\n", 1)[0]
    expected_title = f"# AGENTS.md — {entry.get('profession', '')} Agent"
    if title != expected_title:
        error(f"{where}/AGENTS.md", f"title should be '{expected_title}', found '{title}'")

    for heading in re.findall(r"^## (.+?)[ \t]*$", body, re.M):
        canonical = CANONICAL_BY_KEY.get(heading_key(heading))
        if canonical and canonical != heading:
            error(f"{where}/AGENTS.md", f"heading '## {heading}' should be '## {canonical}'")

    claude_md = folder / "CLAUDE.md"
    if not claude_md.is_file() or claude_md.read_text() != body:
        error(f"{where}/CLAUDE.md", "missing or not byte-identical to AGENTS.md")

    subagent = folder / "agents" / f"{slug}.md"
    if not subagent.is_file():
        error(where, f"missing agents/{slug}.md")
    else:
        match = re.match(r"---\n(.*?)\n---\n(.*)", subagent.read_text(), re.S)
        if not match:
            error(f"{where}/agents/{slug}.md", "missing YAML frontmatter")
        else:
            front, sub_body = match.groups()
            if not re.search(rf"^name: {re.escape(slug)}$", front, re.M):
                error(f"{where}/agents/{slug}.md", f"frontmatter name should be '{slug}'")
            desc = re.search(r"^description: (.*)$", front, re.M)
            try:
                desc_value = json.loads(desc.group(1)) if desc else None
            except json.JSONDecodeError:
                desc_value = desc.group(1)
            if desc_value != summary:
                error(f"{where}/agents/{slug}.md", "frontmatter description differs from catalog summary")
            if sub_body.strip("\n") != body.strip("\n"):
                error(f"{where}/agents/{slug}.md", "body differs from AGENTS.md")

    plugin = folder / ".claude-plugin" / "plugin.json"
    manifest = load_json(plugin) if plugin.is_file() else None
    if plugin.is_file() and manifest is None:
        return None
    if manifest is None:
        error(where, "missing .claude-plugin/plugin.json")
        return None
    if manifest.get("name") != slug:
        error(f"{where}/.claude-plugin/plugin.json", f"name should be '{slug}'")
    if manifest.get("description") != summary:
        error(f"{where}/.claude-plugin/plugin.json", "description differs from catalog summary")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        error(f"{where}/.claude-plugin/plugin.json", "version is not semver")
    return manifest.get("version")


def check_marketplace(catalog, versions):
    data = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    if data is None:
        return
    plugins = data.get("plugins", [])
    names = [p.get("name", "") for p in plugins]
    if names != sorted(names):
        error("marketplace.json", "plugins not sorted by name")
    for name in set(names) - set(catalog):
        error("marketplace.json", f"plugin '{name}' has no catalog entry")
    for slug in set(catalog) - set(names):
        error("marketplace.json", f"no plugin entry for '{slug}'")
    for plugin in plugins:
        slug = plugin.get("name", "")
        entry = catalog.get(slug)
        if entry is None:
            continue
        where = f"marketplace.json:{slug}"
        if plugin.get("source") != f"./scientific-agents/{slug}":
            error(where, f"source should be './scientific-agents/{slug}'")
        if plugin.get("description") != entry["summary"]:
            error(where, "description differs from catalog summary")
        meta = plugin.get("metadata", {})
        if meta.get("profession") != entry["profession"]:
            error(where, "metadata.profession differs from catalog")
        if meta.get("work_mode") != entry["work_mode"]:
            error(where, "metadata.work_mode differs from catalog")
        if versions.get(slug) and plugin.get("version") != versions[slug]:
            error(where, f"version {plugin.get('version')} differs from plugin.json {versions[slug]}")


def check_readme(catalog):
    text = (ROOT / "README.md").read_text()
    total = len(catalog)
    badge = re.search(r"Expert_Profiles-(\d+)-", text)
    if not badge or int(badge.group(1)) != total:
        error("README.md", f"Expert_Profiles badge should say {total}")
    intro = re.search(r"All (\d+) expert profiles", text)
    if not intro or int(intro.group(1)) != total:
        error("README.md", f"'All N expert profiles' should say {total}")

    row_re = re.compile(r"^\| \[(.+?)\]\(scientific-agents/([^/]+)/AGENTS\.md\) \| (.+?) \|\s*$", re.M)
    seen = defaultdict(int)
    sections = re.findall(r"<summary><b>(.+?)</b> — (\d+) profiles</summary>(.*?)</details>", text, re.S)
    if not sections:
        error("README.md", "no domain sections found under Agents")
    for name, count, block in sections:
        rows = row_re.findall(block)
        if len(rows) != int(count):
            error("README.md", f"section '{name}' says {count} profiles but has {len(rows)} rows")
        professions = [r[0] for r in rows]
        if professions != sorted(professions, key=str.lower):
            error("README.md", f"section '{name}' is not sorted alphabetically by profession")
        for profession, slug, summary in rows:
            seen[slug] += 1
            entry = catalog.get(slug)
            if entry is None:
                error("README.md", f"row links to '{slug}', which has no catalog entry")
                continue
            if profession != entry["profession"]:
                error("README.md", f"row for '{slug}' says '{profession}', catalog says '{entry['profession']}'")
            if summary.strip() != entry["summary"]:
                error("README.md", f"row summary for '{slug}' differs from catalog summary")
    for slug in catalog:
        if seen[slug] != 1:
            error("README.md", f"'{slug}' appears in {seen[slug]} rows (expected 1)")


def check_overlap(bodies):
    """Flag pairs of profiles that share a large block of verbatim lines."""
    lines = {}
    for slug, body in bodies.items():
        lines[slug] = {
            line.strip().lower()
            for line in body.splitlines()
            if len(line.strip()) >= 40 and not line.lstrip().startswith("#")
        }
    owners = defaultdict(list)
    for slug, content in lines.items():
        for line in content:
            owners[line].append(slug)
    shared = defaultdict(int)
    for slugs in owners.values():
        # Skip lines nearly every profile has; they are boilerplate, not copying.
        if 1 < len(slugs) < 50:
            for pair in itertools.combinations(sorted(slugs), 2):
                shared[pair] += 1
    for (a, b), count in sorted(shared.items()):
        smaller = min(len(lines[a]), len(lines[b])) or 1
        if count / smaller > MAX_OVERLAP:
            error("scientific-agents", f"'{a}' and '{b}' share {count / smaller:.0%} of their lines verbatim")


def check_skill_copies():
    # The skill folders are gitignored, so a fresh clone has neither; skip then.
    present = [copy for copy in SKILL_COPIES if copy.is_dir()]
    if not present:
        return
    if len(present) == 1:
        missing = next(c for c in SKILL_COPIES if c not in present)
        warn(str(missing.relative_to(ROOT)), "skill copy missing; only one copy exists")
        return
    trees = []
    for copy in SKILL_COPIES:
        trees.append({p.relative_to(copy): p.read_bytes() for p in copy.rglob("*") if p.is_file()})
    first, second = trees
    for rel in sorted(set(first) | set(second)):
        if first.get(rel) != second.get(rel):
            error("skills", f"{rel} differs between .agents/skills and .claude/skills")


def main():
    catalog = check_catalog()
    folders = {p.name for p in PROFILES.iterdir() if p.is_dir()}
    for slug in sorted(folders - set(catalog)):
        error(f"scientific-agents/{slug}", "folder has no catalog entry")
    for slug in sorted(set(catalog) - folders):
        error("catalog.json", f"entry '{slug}' has no scientific-agents/{slug}/ folder")

    versions, bodies = {}, {}
    for slug in sorted(folders & set(catalog)):
        versions[slug] = check_profile(slug, catalog[slug])
        agents_md = PROFILES / slug / "AGENTS.md"
        if agents_md.is_file():
            bodies[slug] = agents_md.read_text()

    check_marketplace(catalog, versions)
    check_readme(catalog)
    check_overlap(bodies)
    check_skill_copies()

    for msg in warnings:
        print(f"warning: {msg}")
    for msg in errors:
        print(f"error: {msg}")
    print(f"\n{len(catalog)} profiles checked: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
