# Chemistry Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 37 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Chemistry.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Analytical Chemist
**Agent file:** `agents/analytical-chemist.md`

Reasons from the chemical measurement process through ICH Q2(R2) and USP <621> validation, CRM traceability, EURACHEM uncertainty budgets, and HPLC/GC/LC-MS/ICP-MS workflows while treating matrix effects, SST drift, peak tailing, and ion suppression as first-class failure modes.

---

### Astrochemist
**Agent file:** `agents/astrochemist.md`

Reasons from gas-grain reaction networks, H₂ ortho/para and CR ionization rates through KIDA/kida.uva.2024, CDMS/JPL/Splatalogue line lists, Nautilus/UCLCHEM gas-grain models, ALMA/JWST/LIDA ice–gas linkage, XCLASS LTE fitting, and line-blending discrimination—not generic chemistry.

---

### Atmospheric Chemist
**Agent file:** `agents/atmospheric-chemist.md`

Reasons from coupled photochemical OH-NOx-VOC radical budgets, heterogeneous aerosol uptake, and NOx-limited versus VOC-limited regimes through MCM/F0AM and GEOS-Chem/CMAQ/WRF-Chem models, OH-reactivity closure, PMF on AMS factors, HYSPLIT trajectories, and EKMA isopleths while treating chamber wall losses, instrument cross-sensitivities and inlet artifacts, and emission-inventory error as first-class failure modes.

---

### Biochemist
**Agent file:** `agents/biochemist.md`

Reasons from thermodynamics, enzyme mechanisms, and binding energetics; designs orthogonal purification and assay readouts while controlling oxidation, aggregation, coupled assays, and activity-vs-abundance confounds.

---

### Biophysical Chemist
**Agent file:** `agents/biophysical-chemist.md`

Reasons from free energy landscapes, binding equilibria (K_d, ΔG = ΔH − TΔS), and probe–system coupling through ITC, SPR/BLI, smFRET, AUC, and global fitting (KinTek, SEDFIT) while treating probe perturbation, mass-transport-limited kon, aggregation-driven avidity, and two-state melting violations as first-class failure modes.

---

### Catalysis Scientist
**Agent file:** `agents/catalysis-scientist.md`

Reasons from active-site structure, turnover frequency, selectivity, and the Sabatier principle through CO/H2 chemisorption site-counting, Weisz-Prater and Mears transport checks, Langmuir-Hinshelwood/Mars-van Krevelen kinetics, and operando DRIFTS/XAS while treating diffusion-limited apparent rates, DRIFTS spectator species, mercury-test false positives for leached Pd, sintering, coking, and selectivity collapse at high conversion as first-class failure modes.

---

### Chemical Biologist
**Agent file:** `agents/chemical-biologist.md`

Reasons from chemical genetics, ABPP/TPP/CETSA chemoproteomics, and SGC/Portal probe criteria; deconvolves phenotypic hits with PAINS/aggregator triage, inactive analogs, and genetic epistasis while treating colloidal aggregation, probe promiscuity, and degrader DC50/Dmax tag artifacts as first-class failure modes.

---

### Cheminformatician
**Agent file:** `agents/cheminformatician.md`

Reasons from Standard InChI identity and RDKit sanitization through ChEMBL pChEMBL harmonization, Morgan/ECFP fingerprints, scaffold splits and applicability domains, while treating tautomer collapse, KNIME-vs-Python canonicalization drift, and random-split QSAR leakage as first-class failure modes.

---

### Colloid Chemist
**Agent file:** `agents/colloid-chemist.md`

Reasons from interfacial thermodynamics, DLVO and non-DLVO forces, zeta-potential, and rheology through orthogonal characterization (DLS, NTA, cryo-TEM, SAXS/SANS S(Q), pendant-drop tensiometry) and accelerated-aging stability tests while treating coalescence, Ostwald ripening, creaming, and flocculation crossing the isoelectric point as first-class failure modes.

---

### Computational Chemist
**Agent file:** `agents/computational-chemist.md`

Reasons from Kohn–Sham DFT, def2/D4 functional selection, and conformer ensembles through VASP/Gaussian/ORCA, AMBER/GROMACS MD, CREST/CENSO sampling, ONIOM/QM/MM electrostatic embedding, GMTKN55 validation, and SCF convergence escalation while treating B3LYP/6-31G*, BSSE, link-atom artifacts, and force-field mismatch as first-class failure modes.

---

### Crystallographer
**Agent file:** `agents/crystallographer.md`

Reasons from reciprocal-space diffraction data, Bragg's law, and space-group symmetry through XDS/DIALS scaling, Phaser/SHELX phasing, Coot/Olex2 building, and MolProbity/checkCIF validation while treating merohedral twinning, wrong space groups, model-bias density unsupported by omit/polder maps, and R_free overfitting as first-class failure modes.

---

### Electrochemist
**Agent file:** `agents/electrochemist.md`

Reason from interfacial thermodynamics and transport: Nernst sets equilibrium, Butler–Volmer sets kinetics, Levich/Randles–Ševčík set mass transport, and EIS deconvolves electrode and battery interphases.

---

### Environmental Chemist
**Agent file:** `agents/environmental-chemist.md`

Reasons from thermodynamic partitioning (K_oc/K_ow, Henry's law), pathway-specific half-lives, and mass balance through GC-MS/LC-MS/MS/ICP-MS analysis, EPI Suite and fugacity fate models, and EPA SW-846 QA/QC while treating blank contamination, matrix suppression, censored sub-LOD data, and unscoped transformation products as first-class failure modes.

---

### Flavor Fragrance Chemist
**Agent file:** `agents/flavor-fragrance-chemist.md`

Reasons from odor activity values, threshold perception, matrix release, and degradation kinetics through GC-MS with retention indices, GC-O/AEDA, chiral GC authentication, ISO 8586 trained sensory panels, and IFRA/FEMA regulatory limits while treating aldehyde oxidation, citral cyclization, top-note fade, and allergen exceedance as first-class failure modes.

---

### Forensic Chemist
**Agent file:** `agents/forensic-chemist.md`

Reasons from chain of custody, validated methods, measurement uncertainty, and class-versus-individual characteristics through GC-MS, LC-MS/MS, FTIR, and SWGDRUG-aligned identification under ISO/IEC 17025, while treating carryover contamination, secondary transfer, isomer co-elution, and upgrading equivocal results into source attribution as first-class failure modes.

---

### Geochemist
**Agent file:** `agents/geochemist.md`

Reasons from Gibbs equilibria, mass and isotope balance, and fluid–rock interaction through stable (δ) and radiogenic (ε, isochron) systems, ICP-MS/LA-ICP-MS/TIMS/MC-ICP-MS/IRMS, PHREEQC/Perple_X phase modeling, and EarthChem/GeoReM workflows while treating alteration, matrix effects, Pb loss, mixing arrays, and Fretwell’s Law violations as first-class failure modes.

---

### Green Chemist
**Agent file:** `agents/green-chemist.md`

Reasons from Anastas–Warner 12 principles, Trost atom economy, and PMI/MMI/E-factor mass metrics; selects solvents via CHEM21/GSK/ACS GCIPR guides, integrates catalysis and LCA (ISO 14040), and aligns REACH/CSS with ACS GC&E benchmarking.

---

### Inorganic Chemist
**Agent file:** `agents/inorganic-chemist.md`

Reasons from electron counting, ligand field theory, and HSAB matching through Schlenk/glovebox air-sensitive synthesis, SCXRD/checkCIF validation, Evans/EPR/XANES oxidation-state assignment, and hot-filtration leaching tests while treating paramagnetic NMR overinterpretation, mystery-oil misidentification, and DFT-without-multiplicity claims as first-class failure modes.

---

### Isotope Geochemist
**Agent file:** `agents/isotope-geochemist.md`

Reasons from fractionation theory, decay schemes, reservoir mixing, and closure assumptions through standard-sample bracketing, double-spike deconvolution, isochron/Tera-Wasserburg fitting with MSWD, and ISO Guide uncertainty propagation while treating Pb-blank and lab-air contamination, mass bias, Pb loss and inheritance, and open-system resetting as first-class failure modes.

---

### Mass Spectrometrist
**Agent file:** `agents/mass-spectrometrist.md`

Reasons from ion formation, m/z resolution and mass accuracy, fragmentation, and calibrated ion statistics through ESI/APCI/MALDI tuning, CID/HCD/ETD MS/MS, isotope-pattern formula assignment, and spectral libraries (NIST, mzCloud, GNPS) under FDA/ICH M10/MSI tiers, while treating matrix suppression, PEG/siloxane/keratin contamination, decoy-driven FDR inflation, and unassigned adducts as first-class failure modes.

---

### Materials Chemist
**Agent file:** `agents/materials-chemist.md`

Reasons from Kröger–Vink defect equilibria, soft-chemistry routes (sol-gel, hydrothermal, ALD), and structure–property links; validates with GSAS-II/TOPAS Rietveld QPA, GIPAW ssNMR, ICSD/COD/Materials Project, and XPS/BET protocols while treating preferred orientation, AdC mis-referencing, degas artifacts, and metastable phase traps as first-class failure modes.

---

### Medicinal Chemist
**Agent file:** `agents/medicinal-chemist.md`

Reasons from structure-activity relationships, lipophilicity and unbound-fraction physicochemistry, synthetic accessibility, and target-product-profile multiparameter optimization through LLE/Fsp3/QED scoring, FEP+/Glide docking validated against co-crystal and SPR data, ELN-tracked LC-MS/NMR synthesis, and DMPK panels (microsomal CL, Caco-2 efflux, hERG, CYP) while treating PAINS and aggregation assay artifacts, biochemical-versus-cellular potency gaps, reactive-metabolite soft spots, and freedom-to-operate cliffs as first-class failure modes.

---

### Natural Products Chemist
**Agent file:** `agents/natural-products-chemist.md`

Reasons from dereplication (GNPS FBMN, NPAtlas, SNAP-MS, COCONUT), bioassay-guided and MS-triggered isolation, NMR/HRMS structure tiers (DP4+/DU8+), antiSMASH/MIBiG BGC linkage, and PAINS/IMP assay interference while treating HMBC ambiguity, stereochemical misassignment, and aggregator false positives as first-class failure modes.

---

### Nuclear Chemist
**Agent file:** `agents/nuclear-chemist.md`

Reasons from decay-corrected activity ledgers, decay modes and cross sections, and ALARA dose control through Bateman/ORIGEN modeling, extraction-chromatography separations (TRU/Sr/TEVA resins), and HPGe/alpha/LSC spectroscopy while treating daughter ingrowth, generator breakthrough, spectral pile-up and sum peaks, and swipe-test cross-contamination as first-class failure modes.

---

### Organic Chemist
**Agent file:** `agents/organic-chemist.md`

Reasons from retrosynthesis, protecting-group strategy, and stereoelectronics; executes air-sensitive chemistry, flash/LC-MS purification, and NMR/IR/MS proof; mines SciFinder/Reaxys and reports ACS-grade experimentals with E-factor/PMI and pyrophoric safety discipline.

---

### Organometallic Chemist
**Agent file:** `agents/organometallic-chemist.md`

Reasons from electron counting, oxidation states, and elementary catalytic steps through Schlenk/glovebox technique, multinuclear NMR and νCO IR, SCXRD with checkCIF, and TON/TOF kinetics while treating air oxidation to oxo/hydroxo species, paramagnetic line-broadening, and trace or colloidal-metal leaching as first-class failure modes.

---

### Petrochemist
**Agent file:** `agents/petrochemist.md`

Reasons from boiling range, hydrocarbon class, sulfur/nitrogen speciation, and octane/cetane drivers through SimDist and PIONA/SARA group-type analysis, CFR-engine RON/MON and cetane testing, refinery LP models, and ASTM/EN spec methods, while treating light-ends loss, assay mismatch versus plant yields, catalyst end-of-run deactivation, and asphaltene instability as first-class failure modes.

---

### Photochemist
**Agent file:** `agents/photochemist.md`

Reasons from Jablonski diagrams, quantum yields, and excited-state potential energy surfaces through ferrioxalate actinometry, TCSPC and transient-absorption flash photolysis, Stern–Volmer quenching, and TDDFT/CASPT2 calculations while treating inner-filter distortion, oxygen-sensitive triplet pathways, photodegradation mistaken for reaction, and emission from impurities as first-class failure modes.

---

### Physical Chemist
**Agent file:** `agents/physical-chemist.md`

Reasons from state functions, partition functions, rate laws, and selection rules through Eyring and van't Hoff fits, DSC/ITC calorimetry, and stopped-flow spectroscopy anchored to NIST thermochemical data, while treating inner-filter and aggregation artifacts, curved Arrhenius plots from mechanism change, and concentration-for-activity substitution as first-class failure modes.

---

### Polymer Chemist
**Agent file:** `agents/polymer-chemist.md`

Designs and interprets polymer synthesis, characterization, and structure–property relationships from mechanism (chain-growth, step-growth, RDRP, ROMP) through absolute MW verification to application-relevant thermal and rheological data.

---

### Process Chemist
**Agent file:** `agents/process-chemist.md`

Reasons from mass and energy balances, impurity fate maps, and supersaturation trajectories through RC1 calorimetry, DoE in JMP/MODDE, FBRM/XRPD crystallization tracking, and ICH Q8/Q9/Q11 control strategy while treating exotherm runaway at plant jacket capacity, ICH M7 genotoxic carry-over, polymorph shifts on scale, and unvalidated PAT release as first-class failure modes.

---

### Quantum Chemist
**Agent file:** `agents/quantum-chemist.md`

Reasons from the Schrödinger equation through HF, MP2/CCSD(T)/CBS, and multireference (CASSCF/CASPT2); uses ORCA/Psi4/Gaussian with GMTKN55/WTMAD-4 validation, T1/D1 diagnostics, Helgaker CBS extrapolation, and BSSE/spin-contamination checks while treating SCF near-degeneracy, intruder states, and global-vs-local multireference masking as first-class failure modes.

---

### Radiochemist
**Agent file:** `agents/radiochemist.md`

Reasons from radionuclide half-life, specific activity, radiochemical purity, and dosimetry through analytical/prep HPLC with radiodetector, iTLC, HPGe γ-spectroscopy, OLINDA/MIRD, and USP <823>/EANM release specs while treating defluorination, transchelation of ⁶⁸Ga/⁸⁹Zr, ⁹⁹ᵐTc colloid and ⁶⁸Ge breakthrough as first-class failure modes.

---

### Spectroscopist
**Agent file:** `agents/spectroscopist.md`

Reasons from selection rules, line shapes as convolutions of intrinsic and instrument broadening, and Beer-Lambert linearity through UV-Vis, fluorescence, IR/Raman, NMR, CD, EPR, and XAS/XPS with calibration standards (polystyrene 1601 cm⁻¹, TMS/DSS, C 1s 284.8 eV) while treating inner filter effects, baseline artifacts inventing peaks, Fermi resonances, and X-ray beam damage as first-class failure modes.

---

### Supramolecular Chemist
**Agent file:** `agents/supramolecular-chemist.md`

Reasons from noncovalent binding free energies (ΔG = ΔH − TΔS), host-guest complementarity, and cooperative assembly through ITC, NMR titration with global fitting (Bindfit, SupraFit), Job's method, and SCXRD while treating wrong-stoichiometry K fits, kinetic traps mistaken for thermodynamic products, ITC dilution-dominated heats, and crystal packing assumed to dominate solution as first-class failure modes.

---

### Surface Chemist
**Agent file:** `agents/surface-chemist.md`

Reasons from interfacial thermodynamics, Langmuir/BET/D-R adsorption, and Young–Dupré wetting through XPS (ISO 15472/18118, AdC vacuum-level alignment, SESSA), contact-angle SFE (OWRK/vOCG, ASTM D7490), QCM-D viscoelastic modeling, ToF-SIMS, SAMs, and ISO 20579 handling while treating adventitious carbon, charging, siloxane contamination, Cassie–Wenzel states, and tip convolution as first-class failure modes.

---

### Theoretical Chemist
**Agent file:** `agents/theoretical-chemist.md`

Reasons from Hamiltonians, partition functions, and flux through dividing surfaces using validated potential energy surfaces, variational transition state theory with Eckart and small-curvature tunneling (Polyrate), and master-equation falloff solvers (MESMER, MultiWell), while treating spurious saddle imaginary modes, spin contamination, recrossing, and silent single-surface MD across conical intersections as first-class failure modes.

---

