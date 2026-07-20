# Contributing to Scientific Agents

Thanks for helping grow this collection. This repo holds **expert-thinking
profiles**: one `AGENTS.md` per scientific or engineering profession, each
teaching an AI agent to reason like a senior practitioner in that field.

There are two ways to contribute:

1. **Request or report** — open an issue to request a new profession or flag a
   problem with an existing profile. No writing required.
2. **Author** — open a pull request that adds a new profile or improves an
   existing one.

Both are welcome. If you only have 30 seconds, an issue is genuinely useful.

---

## The one thing that matters: specificity

Every profile lives or dies by one test, the **generic-swap test**:

> Read any sentence in the profile. Mentally swap in a *different* profession's
> name. If the sentence still reads as true, it is filler — cut it or replace it
> with a real specific.

- ❌ *"Always use rigorous statistical methods and think critically."* — true for
  everyone → **cut.**
- ✅ *"Correct GWAS p-values for genome-wide significance at 5×10⁻⁸."* — true only
  for this field → **keep.**

A strong profile names the field's actual databases, instruments, units,
controls, thresholds, standards, journals, and **named failure modes** — the
things a practitioner would recognize as true and useful and an outsider could
not have written. A weak profile is a "be rigorous, be careful" essay wearing a
profession's name tag. We only merge the former.

The house style for the one-line summary (used in `catalog.json`, the README
table, and the plugin description) is a single dense sentence:

> *Reasons from `<first-principles foundations>` through `<specific named tools,
> methods, standards>` while treating `<3–5 specific, field-distinctive failure
> modes>` as first-class failure modes.*

Look at existing entries in [`catalog.json`](catalog.json) before writing yours.

---

## Reporting a problem or requesting a profession

Open an issue using one of the templates:

- **New expert profile** — name the profession, sub-specialty, and (if you know
  the field) a few concrete tools/databases/failure modes that a good profile
  must include. That head start meaningfully improves the result.
- **Profile correction** — point to the file and line, describe what's wrong
  (a wrong tool name, an out-of-date threshold, a missing failure mode), and
  cite a source if you have one. **Wrong specifics are worse than honest gaps**,
  so these reports are high-value.

---

## Authoring a profile (pull request)

### Recommended path: the skill

Profiles are normally generated with the **`create-scientific-agent`** skill,
which runs the required multi-source research, applies the quality bar, fills the
template, and updates every registry. If you have access to it (it ships with
K-Dense's Claude Code tooling), use it — it handles the mechanics below for you.
The rest of this section is what the skill does, written out so a profile can be
authored or reviewed by hand.

### What a profile must contain

Write `AGENTS.md` in the **second person** ("You are…", "When you…"), dense and
scannable — headers and bullets, no filler. Ground it in real research (name your
sources); internal knowledge alone produces plausible-but-generic profiles, and
the gap shows. Cover, in the field's own terms:

- **Mindset / first principles** the agent reasons *from*, not just recalls.
- **Problem-framing**, including the field's named red herrings.
- **Workflow** — how the field actually sequences work.
- **Tools / instruments / software** — named, with when-to-use and gotchas.
- **Data / databases / literature** — named and findable.
- **Controls** — the field's actual positive and negative controls.
- **Statistics & uncertainty** — dominant methods, error model, units, reporting.
- **Confounders / threats to validity** specific to the field.
- **Troubleshooting** — named artifacts and failure modes, and how to detect each.
- **Communication** — reporting structure, figure norms, hedging register,
  standards by name.
- **Units, ethics, vocabulary** the agent must get right.

Existing profiles run ~10–48 KB. Length must be **earned by specificity**, never
padded.

### File layout

Each profession is a directory under `scientific-agents/<slug>/`, where `<slug>`
is the profession as a **kebab-case** slug (e.g. `tissue-engineer`,
`clinical-epidemiologist`). A complete profile contains **four files**:

```
scientific-agents/<slug>/
├── AGENTS.md                     # the profile (source of truth)
├── CLAUDE.md                     # byte-identical copy of AGENTS.md
├── .claude-plugin/plugin.json    # plugin manifest (name, version, description)
└── agents/<slug>.md              # subagent file: frontmatter (name, description) + body
```

The `description` in `plugin.json` and the frontmatter `description` in
`agents/<slug>.md` must both be the profile's one-line summary (see house style
above). `CLAUDE.md` must be identical to `AGENTS.md`.

### Registries to keep in sync

Three shared files index every profile and **must never drift**. Update all of
them in the same PR:

1. **[`catalog.json`](catalog.json)** — add/update the entry under `agents`,
   sorted by `slug`:

   ```json
   {
     "profession": "Tissue Engineer",
     "slug": "tissue-engineer",
     "path": "tissue-engineer/AGENTS.md",
     "work_mode": "wet-lab / regenerative medicine",
     "summary": "Reasons from … while treating … as first-class failure modes.",
     "created": "YYYY-MM-DD",
     "updated": "YYYY-MM-DD",
     "source_count": 0
   }
   ```

2. **[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)** — add
   the plugin entry (`name`, `source`, `description`, `version`, `category`,
   `keywords`, `metadata`) matching the other entries.

3. **[`README.md`](README.md)** — add a row to the correct domain table:
   `| [Profession](scientific-agents/<slug>/AGENTS.md) | one-line summary |`,
   keeping each table sorted alphabetically. Then bump: the profile count in that
   domain's `<summary>`, the total in the intro sentence, and the
   `Expert_Profiles` number in the badge at the top of the file.

   Domains: Mathematics & Statistics · Computer Science, Data & AI · Physics ·
   Astronomy & Space Science · Chemistry · Materials, Nanoscience & Energy ·
   Earth, Environmental & Atmospheric Science · Biology & Life Sciences ·
   Medicine & Clinical Science · Agriculture, Food & Veterinary Science ·
   Engineering.

> The one-line summary must be **identical** in `catalog.json`, `README.md`,
> `marketplace.json`, `plugin.json`, and `agents/<slug>.md`.

When regenerating an existing profile, update its entries **in place** (refresh
`updated`, `summary`, `source_count`) rather than adding duplicates.

### Clean up

Delete any temporary files created during research or drafting (including any
`.json` scratch files from search/research tooling) before committing.

---

## Pull request checklist

Copy this into your PR description and tick each box:

- [ ] `AGENTS.md` passes the generic-swap test top to bottom — no filler lines.
- [ ] Specifics are **real** (named tools, databases, thresholds, standards). No
      invented specifics; honest gaps over wrong facts.
- [ ] Second person, scannable, no padding.
- [ ] All four per-profile files present and consistent (`AGENTS.md`,
      identical `CLAUDE.md`, `plugin.json`, `agents/<slug>.md`).
- [ ] Same one-line summary in all five places (catalog, README, marketplace,
      plugin.json, agents file).
- [ ] `catalog.json` entry added/updated and sorted by `slug`; JSON valid.
- [ ] `marketplace.json` entry added/updated; JSON valid.
- [ ] README table row added (sorted), and all three counts bumped (domain
      `<summary>`, intro total, badge).
- [ ] Temporary/scratch files removed.

Thanks again — every well-researched profile makes the whole collection more
useful.
