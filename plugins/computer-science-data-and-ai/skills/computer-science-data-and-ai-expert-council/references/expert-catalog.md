# Computer Science, Data & AI Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 30 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Computer Science, Data & AI.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Ai Researcher
**Agent file:** `agents/ai-researcher.md`

Reasons from data generating processes, inductive biases, and compute-data-algorithm trade-offs through train/val/test discipline, seed sweeps, ablation ladders, and standards like NeurIPS reproducibility checklists, model cards, and lm-eval-harness, while treating data leakage (Kapoor & Narayanan taxonomy), benchmark contamination, spurious correlations, and reward-model overoptimization as first-class failure modes.

---

### Algorithms Researcher
**Agent file:** `agents/algorithms-researcher.md`

Reasons from separating problem, model, and cost model (comparison, word-RAM, arithmetic, online) through exchange/matroid greedy proofs, subproblem-DAG dynamic programming, max-flow min-cut and Goemans–Williamson primal-dual rounding, Karp–Rabin fingerprinting, competitive ratio and Yao's principle, PTAS/FPTAS (Williamson–Shmoys), and Instance Space Analysis over DIMACS10/MIPLIB 2017/SuiteSparse while treating amortized-versus-average-case conflation, unproven greedy killed by a 4-node counterexample, Monte Carlo without a false-match probability, DIMACS10 suite overfitting, and 'linear time' hiding word-size tricks over bit-length L as first-class failure modes.

---

### Computational Linguist
**Agent file:** `agents/computational-linguist.md`

Reasons from UD/PTB formalisms, validate.py/eval.py (LAS/MLAS/ELAS), and evalb .prm settings through Stanza/UDPipe pipelines, PropBank/FrameNet/AMR/UMR layers, IAA (κ, Krippendorff α), CONDA contamination checks, and ARR reproducibility while treating tokenizer mismatch, oracle inflation, train–test leakage, and guideline drift as first-class failure modes.

---

### Computational Scientist
**Agent file:** `agents/computational-scientist.md`

Reasons from Roache code/solution verification and ASME V&V 10/20/40 credibility through MMS/GCI, UQ ensembles, and Snakemake/Nextflow/CWL pipelines with conda-lock/Apptainer provenance while treating environment drift, workflow cache staleness, and validation-vs-calibration conflation as first-class failure modes.

---

### Computational Social Scientist
**Agent file:** `agents/computational-social-scientist.md`

Reasons from social mechanisms, measurement validity, and sampling frames through DAGs, fixed-effects and IV/DiD/RDD designs, ERGM/SAOM network models, and human-audited text classifiers while treating unobserved homophily, network interference and SUTVA violations, platform-driven selection, bot contamination, and digital-skew unrepresentativeness as first-class failure modes.

---

### Computer Architecture Researcher
**Agent file:** `agents/computer-architecture-researcher.md`

Reasons from ISA semantics, AMAT/CPI, MESI coherence, and branch prediction through gem5/SPEC/MLPerf evaluation, Amdahl and roofline discipline, TPU/GPU dataflow accelerators, DVFS/EDP, and Spectre/Meltdown mitigation overhead at ISCA/MICRO/HPCA rigor.

---

### Computer Graphics Researcher
**Agent file:** `agents/computer-graphics-researcher.md`

Reasons from the rendering equation and Monte Carlo MIS through Mitsuba/Embree/Blender, Vulkan/DXR real-time stacks, BRDF/BSDF validation, SIGGRAPH/EG reporting, NeRF/3DGS pitfalls, OCIO color pipelines, OIDN denoising bias, and mesh/UV artifact diagnosis while treating train–display gamma errors and unequal-spp comparisons as first-class failure modes.

---

### Computer Scientist
**Agent file:** `agents/computer-scientist.md`

Reasons from computational models, abstraction contracts, invariants, and measurable complexity through CLRS-grade algorithm analysis, impossibility results (FLP, CAP, NP-hardness), property-based and chaos testing, and formal tools (TLA+, Coq, Z3) while treating partial failure, race conditions, label leakage, and abstraction leaks like GC pauses and clock skew as first-class failure modes.

---

### Computer Security Researcher
**Agent file:** `agents/computer-security-researcher.md`

Reasons from explicit threat models and CIA/STRIDE through AFL++/libFuzzer triage, ASan/KASAN oracles, ProVerif/Tamarin proofs, CVE/CWE/CAPEC taxonomies, CyberGym dual-execution benchmarks, Menlo/CVD ethics, and USENIX open-science artifact norms.

---

### Computer Vision Scientist
**Agent file:** `agents/computer-vision-scientist.md`

Reasons from calibration, augmentations, and domain shift through COCO/LVIS/KITTI metrics (mAP, IoU, mask AP), convnets vs ViTs, OpenCV/PyTorch/MMDetection stacks, COLMAP/NeRF 3D, and CVPR/ICCV/ECCV eval discipline while treating label noise, train-test leakage, and resolution mismatch as first-class failure modes.

---

### Cryptographer
**Agent file:** `agents/cryptographer.md`

Reasons from IND-CCA/EUF-CMA games and tight reductions through AES-GCM/RSA-OAEP/ECDSA, ML-KEM/ML-DSA (FIPS 203/204), ProVerif/Tamarin/EasyCrypt, dudect constant-time, CAVP/ACVP and FIPS 140-3 CMVP—not pure number theory or vuln fuzzing.

---

### Data Engineer
**Agent file:** `agents/data-engineer.md`

Reasons from idempotent ELT, medallion bronze/silver/gold, Kimball grain and SCD2, CDC/Debezium and watermark incremental loads, dbt/GX quality gates, Airflow/Dagster orchestration, Iceberg/Delta lakehouse MERGE, data contracts and freshness SLIs while treating silent join drops, duplicate amplification, schema drift, and green-DAG-wrong-numbers as first-class failure modes.

---

### Data Scientist
**Agent file:** `agents/data-scientist.md`

Reasons from CRISP-DM business estimands, leakage-safe sklearn Pipelines and nested CV, SQL/warehouse semantic metrics, A/B power and SRM/AA guardrails, causal DAG covariate discipline, and Model Cards/Datasheets while treating train-test leakage, Simpson's paradox, peeking, and PSI>0.25 drift as first-class failure modes.

---

### Database Systems Researcher
**Agent file:** `agents/database-systems-researcher.md`

Reasons from storage hierarchy, concurrency semantics, query-optimization theory, and declared workload models through TPC-C/H, YCSB, and JOB benchmarks, Jepsen/Elle correctness checkers, and perf/blktrace/fio profiling while treating cardinality-estimation plan regressions, tail-latency spikes under skew, unfair fsync-disabled speedups, and benchmark-trick wins as first-class failure modes.

---

### Deep Learning Scientist
**Agent file:** `agents/deep-learning-scientist.md`

Reasons from CNN/Transformer inductive bias, Li et al. loss landscapes, grokking/mode connectivity, and Kaplan/Chinchilla scaling (~20 tokens/param); designs ResNet/ViT/DiT/MoE/FlashAttention stacks with FLOPs-matched ablations; trains AdamW+cosine/WSD via Megatron-FSDP/DeepSpeed; evaluates FID/MMLU-Pro/MMLU-CF with lm-eval decontamination and Pineau/NeurIPS reproducibility checklists.

---

### Distributed Systems Researcher
**Agent file:** `agents/distributed-systems-researcher.md`

Reasons from failure models, consistency contracts, and tail-latency-and-recovery performance through TLA+ model checking, Jepsen and Porcupine linearizability checking, and YCSB/DeathStarBench benchmarking with iptables and kill -9 fault injection, while treating unbounded leases and split-brain, clock skew under NTP, and GC-induced p99 spikes as first-class failure modes.

---

### Edge Embedded Ai Engineer
**Agent file:** `agents/edge-embedded-ai-engineer.md`

Reasons from tensor-arena budgets, full-int8 PTQ with representative calibration, and TFLM/CMSIS-NN or Vela/Ethos-U compile paths through ONNX Runtime QNN HTP and mobile delegates—treating train–serve preprocessing skew, float thresholds on quantized outputs, and NPU operator fallback as first-class failure modes.

---

### Formal Methods Researcher
**Agent file:** `agents/formal-methods-researcher.md`

Reasons from operational semantics and temporal logics through SPIN/TLA+/PRISM, Coq/Lean/Isabelle, Z3/CVC5, refinement and separation logic, vacuity and false-positive diagnosis, and Dafny/F* versus property-based testing boundaries.

---

### High Performance Computing Specialist
**Agent file:** `agents/high-performance-computing-specialist.md`

Reasons from NUMA topology and hybrid MPI+OpenMP+CUDA decomposition through Slurm fairshare/backfill job design, strong/weak scaling (Amdahl/Gustafson), Darshan/mpiP/Nsight profiling, and parallel HDF5/MPI-IO on Lustre while treating I/O storms, collectives bottlenecks, and rank-binding mistakes as first-class failure modes.

---

### Human Computer Interaction Researcher
**Agent file:** `agents/human-computer-interaction-researcher.md`

Reasons from situated context, Fitts/GOMS/KLM, and CHI contribution types; runs contextual inquiry through LMM/CLMM analysis with SUS/NASA-TLX triangulation; uses Prolific/OSF and treats demand characteristics, novelty effects, ordinal misuse, and WEIRD samples as first-class failure modes.

---

### Information Retrieval Scientist
**Agent file:** `agents/information-retrieval-scientist.md`

Reasons from the Probability Ranking Principle, ranked-list utility, and candidate-generation-versus-re-ranking separation through BM25 baselines, dense and cross-encoder retrieval, and TREC-style qrels evaluated with trec_eval and nDCG, while treating position-biased clicks, unjudged-as-nonrelevant pools, analyzer mismatches, and AOL-style search-log re-identification as first-class failure modes.

---

### Knowledge Representation Researcher
**Agent file:** `agents/knowledge-representation-researcher.md`

Reasons from model-theoretic semantics, the expressivity-vs-decidability-vs-scalability tradeoff, and competency questions through OWL 2 profiles, reasoners (HermiT, Pellet, ELK), ROBOT/Protégé pipelines, and SHACL validation while treating unsatisfiable classes, silent OWA-vs-CWA semantic mixing, hallucinated LLM-suggested axioms, and IRI-reuse on bad merges as first-class failure modes.

---

### Machine Learning Engineer
**Agent file:** `agents/machine-learning-engineer.md`

Reasons from feature-store point-in-time joins (Feast/Tecton), Airflow/Kubeflow training pipelines, MLflow registry, Triton/TorchServe/BentoML serving, Evidently/WhyLabs drift and PSI, shadow/canary/A/B rollouts, inference SLAs, and reproducible training hashes while treating train–serve skew, label leakage, and peeking A/B as first-class failure modes.

---

### Machine Learning Researcher
**Agent file:** `agents/machine-learning-researcher.md`

Reasons from population risk, double descent, and inductive bias; enforces sacred test sets, hierarchical ablations, nested CV, and HELM/Dynabench-aware benchmarking; reports with NeurIPS and Pineau reproducibility checklists while treating leakage, meta-overfitting, benchmark contamination, Goodhart gaming, and seed variance as first-class failure modes.

---

### Mlops Engineer
**Agent file:** `agents/mlops-engineer.md`

Reasons from data contracts, feature parity, evaluation gates, and rollback-readiness through MLflow/W&B registries, Feast feature stores, KServe/Triton serving, Great Expectations/TFDV validation, and Evidently PSI/KS drift monitors while treating train-serve skew, data leakage, silent degradation, and schema/concept drift as first-class failure modes.

---

### Natural Language Processing Scientist
**Agent file:** `agents/natural-language-processing-scientist.md`

Reasons from tokenization, data curation (datatrove/NeMo), and evaluation protocols (SacreBLEU/COMET, IFEval, HELM); enforces contamination audits (ConTAM, perplexity separation), paired bootstrap significance, SFT→DPO/RLHF with alignment-tax checks, and ARR/Dodge reproducibility while treating exposure bias, benchmark leakage, prompt-template confounds, and metric gaming as first-class failure modes.

---

### Programming Languages Researcher
**Agent file:** `agents/programming-languages-researcher.md`

Reasons from operational semantics, type-theoretic invariants, and soundness as preservation-plus-progress through Ott/LN-defined calculi, Coq/Isabelle/Agda mechanization, Hindley-Milner inference, and abstract-interpretation Galois connections while treating stuck terms, blame escaping onto well-typed pure terms, broken substitution and canonical-forms lemmas, and unsound widening as first-class failure modes.

---

### Reinforcement Learning Researcher
**Agent file:** `agents/reinforcement-learning-researcher.md`

Reasons from MDP/POMDP and Bellman operators through DQN/PPO/SAC/TD3, MuJoCo/Atari/Procgen/Brax benchmarks, offline RL (CQL/IQL), reward-hacking diagnostics, Gymnasium/CleanRL/SB3 stacks, and NeurIPS/ICML/CoRL seed-stratified evaluation with bootstrap CIs.

---

### Research Software Engineer
**Agent file:** `agents/research-software-engineer.md`

Reasons from Software Carpentry and FAIR4RS through SemVer releases, CITATION.cff/SPDX metadata, pytest/Hypothesis CI gates, Docker/Apptainer on Slurm, and maintainability discipline for citable, reproducible research code.

---

### Theoretical Computer Scientist
**Agent file:** `agents/theoretical-computer-scientist.md`

Reasons from explicit models (TM, circuit, communication, query) and resource measures; audits Karp/parsimonious/gap/fine-grained reductions against ETH/SETH/#ETH and PCP/UGC/APX barriers; uses Complexity Zoo, ECCC/arXiv cs.CC, Coq/Lean/DRAT, Williams algorithms-for-lower-bounds, and Yao/IC lower bounds while treating wrong reduction direction, non-parsimony, APSP–3SUM conflation, oracle overclaim, and natural-proofs misuse as first-class failure modes.

---

