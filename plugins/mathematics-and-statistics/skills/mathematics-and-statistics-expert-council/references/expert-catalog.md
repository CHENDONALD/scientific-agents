# Mathematics & Statistics Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 25 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Mathematics & Statistics.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Actuarial Scientist
**Agent file:** `agents/actuarial-scientist.md`

Reasons from mortality tables (qx, period/cohort, select/ultimate) and Chain-Ladder/Mack reserving through GLM/GAM frequency–severity and Tweedie pricing, limited-fluctuation and Bühlhmann-Straub credibility, Solvency II SCR standard formula, and IFRS 17 CSM/RA while treating triangle truncation, overfitting, and tail risk as first-class failure modes.

---

### Algebraist
**Agent file:** `agents/algebraist.md`

Reasons from carriers, operations, and morphisms through isomorphism theorems, universal properties, exact-sequence and homological tools (Ext, Tor, snake lemma), and computational systems like GAP, Magma, SageMath, and Lean while treating silently smuggled hypotheses (commutativity, units, Noetherian, algebraically closed base), characteristic-p false friends, and noncanonical isomorphisms as first-class failure modes.

---

### Applied Mathematician
**Agent file:** `agents/applied-mathematician.md`

Reasons from formulation-first modeling, Buckingham scaling, and asymptotics (matched expansions, boundary layers) through FEM/FVM numerics (FEniCS, PETSc, LAPACK), Tikhonov inverse problems, and ASME/Sandia V&V while treating ill-posed inversion, stiffness, and numerical diffusion as first-class failure modes.

---

### Astrostatistician
**Agent file:** `agents/astrostatistician.md`

Reasons from selection functions, censored flux limits, and look-elsewhere trial factors through Cobaya/emcee/dynesty cosmology, GP-coupled exoplanet inference, Landy–Szalay clustering, photo-z σNMAD calibration, and SBI (sbi/LtU-ILI) while treating Malmquist bias, prior-driven tensions, and detrend-then-fit transit bias as first-class failure modes.

---

### Bayesian Statistician
**Agent file:** `agents/bayesian-statistician.md`

Reasons from Bayes' rule, coherent uncertainty, exchangeability, and partial-pooling hierarchy through Stan/PyMC HMC-NUTS fits, prior and posterior predictive checks, PSIS-LOO, and SBC calibration while treating divergent transitions and funnels, weak identifiability and label switching, improper posteriors, and post-hoc prior tuning as first-class failure modes.

---

### Biostatistician
**Agent file:** `agents/biostatistician.md`

Reasons from estimands, SAPs, and error budgets; aligns ICH E9(R1), CONSORT/STROBE, multiplicity, MMRM, Cox survival, causal DAGs, and GWAS FDR while treating immortal time, ICEs, and batch confounding as first-class failure modes.

---

### Causal Inference Scientist
**Agent file:** `agents/causal-inference-scientist.md`

Reasons from structural causal models, potential outcomes, and identification logic through DAGs and do-calculus, doubly-robust estimators (AIPW/TMLE, IPTW, g-formula), and design-based methods (IV, RD, Callaway-Sant'Anna DiD, synthetic control) while treating colliders and M-bias, positivity/overlap failure, and unmeasured confounding (Rosenbaum bounds, E-values) as first-class failure modes.

---

### Combinatorialist
**Agent file:** `agents/combinatorialist.md`

Reasons from labelled vs unlabelled enumeration, EGF/OGF and species, bijective and probabilistic proofs, Turán/Ramsey/extremal bounds, and BIBD/OA design parameters through SageMath/GAP/nauty, OEIS, House of Graphs, and Colbourn–Dinitz tables while treating isomorphism double-counting, parity barriers, and OEIS false matches as first-class failure modes.

---

### Differential Geometer
**Agent file:** `agents/differential-geometer.md`

Reasons from connections, curvature, and holonomy; fixes Lee vs Besse/MTW Riemann signs; uses SageManifolds/xAct/Cadabra, Chern–Weil and Atiyah–Singer index theory, and model-space checks (S^n, flat tori) while treating chart artifacts, torsion misuse, and CAS convention drift as first-class failure modes.

---

### Dynamical Systems Theorist
**Agent file:** `agents/dynamical-systems-theorist.md`

Reasons from state spaces, invariant sets, bifurcations, and multiple time scales through normal-form classification, center-manifold reduction, Floquet/Poincaré maps, and continuation tools like AUTO, MatCont, and DynamicalSystems.jl while treating spurious chaos from finite-time Lyapunov bias, false limit cycles mistaken for tori, numerical blow-up versus true singularity, and Takens embedding artifacts as first-class failure modes.

---

### Logician
**Agent file:** `agents/logician.md`

Reasons from syntax-versus-semantics and object-versus-metalanguage discipline, the ⊢/⊨ distinction, and matching each logic to its intended semantics through natural deduction and sequent calculus (cut-elimination, subformula property), compactness and Löwenheim–Skolem, forcing and diagonalization, and proof assistants (Lean 4/mathlib, Coq, Isabelle/HOL, Agda) with Z3/CVC5/Vampire/Mace4 automation while treating use–mention conflation, second-order misuse of compactness, mis-stated incompleteness hypotheses (ω-consistency vs consistency), and Gödel philosophical overreach as first-class failure modes.

---

### Mathematical Analyst
**Agent file:** `agents/mathematical-analyst.md`

Reasons from function-space topology, convergence modes, and constant-dependent inequalities (Hölder, Sobolev, Gronwall) through compactness theorems (Rellich-Kondrachov, Banach-Alaoglu), Calderon-Zygmund and Schauder estimates, and Lax-Milgram while treating limit-integral swaps without dominated convergence, boundary-degenerating constants, weak-versus-classical regularity gaps, and concentration-compactness loss as first-class failure modes.

---

### Mathematical Modeler
**Agent file:** `agents/mathematical-modeler.md`

Reasons from nondimensionalization, conservation/positivity laws, and minimal-viable model structure through mechanistic ODE/PDE, stochastic, and agent-based formulations, profile-likelihood and Fisher-information identifiability, and Sobol/Morris sensitivity analysis, while treating sloppy unidentifiable parameters, structural model uncertainty, and out-of-regime extrapolation as first-class failure modes.

---

### Mathematical Physicist
**Agent file:** `agents/mathematical-physicist.md`

Reasons from Hilbert-space domains, Wightman/OS and Haag–Kastler axioms, constructive QFT, Gibbs measures, and spectral/scattering theory; uses Reed–Simon, Glimm–Jaffe, MathSciNet/math-ph, while treating wrong self-adjoint extensions, invalid Wick rotation, limit-order swaps, and lattice-as-continuum claims as first-class failure modes.

---

### Mathematical Statistician
**Agent file:** `agents/mathematical-statistician.md`

Reasons from LAN, empirical processes, and influence functions; proves M/Z-estimator limits, minimax rates (Fano/Le Cam/Assouad), and semiparametric efficiency while validating with ADEMP simulations and treating naive bootstrap, non-Donsker classes, and debiasing sparsity violations as first-class failure modes.

---

### Network Scientist
**Agent file:** `agents/network-scientist.md`

Reasons from adjacency structure, generative models, and null hypotheses through configuration-model and SBM/ERGM nulls, CSN power-law fitting with log-normal Vuong tests, and multi-algorithm community detection (Louvain, Leiden, Infomap, graph-tool) while treating artifactual scale-free tails from correlation thresholding, modularity's resolution bias, force-directed hairball over-interpretation, and test-edge leakage in link prediction as first-class failure modes.

---

### Nonlinear Dynamics Chaos Scientist
**Agent file:** `agents/nonlinear-dynamics-chaos-scientist.md`

Reasons from flows, maps, bifurcations, and invariant sets; continues with MatCont/AUTO/COCO, validates chaos with IAAFT surrogates and embedding convergence, and treats spurious Lyapunov exponents, stiff integrator artifacts, and colored-noise confounds as first-class failure modes.

---

### Number Theorist
**Agent file:** `agents/number-theorist.md`

Reasons from primes, congruences, L-functions, and the Langlands web; chooses algebraic, analytic, and sieve methods; validates with SageMath/PARI/LMFDB while treating PARI stack overflows, conditional-proof leaks, and CRT moduli errors as first-class failure modes.

---

### Numerical Analyst
**Agent file:** `agents/numerical-analyst.md`

Reasons from well-posedness, discretization, conditioning, and stability; verifies codes with MMS and convergence studies; treats cancellation, stiffness, and solver tolerance floors as first-class failure modes.

---

### Operations Researcher
**Agent file:** `agents/operations-researcher.md`

Reasons from decision structure, integrality and convexity, and explicit uncertainty through LP/MIP solvers (Gurobi, CPLEX, OR-Tools CP-SAT), stochastic and Wasserstein-distributionally-robust formulations, and DES (SimPy, AnyLogic) benchmarked on Solomon/MIPLIB instances, while treating unit inconsistencies, optimality-gap-versus-stale-data trade-offs, infeasibility (IIS) from forgotten labor and fairness constraints, and day-to-day solution oscillation as first-class failure modes.

---

### Optimization Scientist
**Agent file:** `agents/optimization-scientist.md`

Reasons from convexity class, KKT/complementarity, and LP/MIP relaxation gaps through interior-point and branch-and-cut (Gurobi, CPLEX, MOSEK, Ipopt) while treating loose big-M, IntegralityTol cheaters, IIS-hidden infeasibility, nonconvex KKT-as-global, and MIPGap-at-TimeLimit-as-optimal as first-class failure modes.

---

### Probabilist
**Agent file:** `agents/probabilist.md`

Reasons from Kolmogorov measure spaces through LLN/CLT, martingales, coupling, concentration/LDP, and Lévy/Feller/Itô calculus; uses Durrett/Kallenberg canon, Sage/NumPy/PyMC simulation, and R̂/ESS/IS diagnostics while treating a.s. vs sure, Borel conditioning, OST misuse, and importance-weight explosion as first-class failure modes.

---

### Pure Mathematician
**Agent file:** `agents/pure-mathematician.md`

Reasons from definitions, axioms, and proved theorems through lemma-ladder proof strategies, computer algebra (SageMath, GAP, Magma) and proof assistants (Lean 4/mathlib, Coq, Isabelle/HOL) checked against MathSciNet/zbMATH and OEIS, while treating hidden hypotheses, circular reasoning, unjustified w.l.o.g. steps, and ZFC-independence as first-class failure modes.

---

### Statistician
**Agent file:** `agents/statistician.md`

Reasons from estimands, generative-model assumptions, and a budgeted Type I/II error tradeoff through analysis plans (SAP, ICH E9(R1) estimands), mixed models, multiple imputation under MCAR/MAR/MNAR, and Benjamini-Hochberg FDR while treating naive post-selection SEs, unadjusted multiplicity, ignored clustering in survey PSUs, and sequential peeking as first-class failure modes.

---

### Topologist
**Agent file:** `agents/topologist.md`

Reasons from continuity, compactness, connectedness, homotopy, and manifold structure through invariants and tools like π₁ via Seifert-van Kampen, cellular/simplicial homology with ∂²=0 and Smith-normal-form torsion, Mayer-Vietoris, and SnapPy/GUDHI computation, while treating lost-Hausdorffness in quotients, torsion missed by rational coefficients, visual deformation without a homotopy or Reidemeister proof, and barcodes interpreted without filtration stability as first-class failure modes.

---

