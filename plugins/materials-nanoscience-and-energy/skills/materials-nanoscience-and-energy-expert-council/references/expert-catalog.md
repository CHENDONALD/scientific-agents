# Materials, Nanoscience & Energy Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 22 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Materials, Nanoscience & Energy.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Biomaterials Scientist
**Agent file:** `agents/biomaterials-scientist.md`

Reasons from material-biology interfaces, degradation-product toxicity, and mechanical mismatch to host tissue through ISO 10993 biological evaluation plans, ISO 10993-12 extract conditions, GPC/ICP/SEM characterization, and sterilization validation while treating endotoxin contamination, pH shift from acidic degradation, extract-ratio artifacts, and non-final-form test articles as first-class failure modes.

---

### Ceramics Engineer
**Agent file:** `agents/ceramics-engineer.md`

Reasons from crystal chemistry, defect equilibria, sintering densification, and flaw statistics through XRD/Rietveld, dilatometry, SEM fractography, impedance spectroscopy, and Weibull analysis per ASTM C1161/C1239/C1421 while treating surface grinding flaws, Pb/alkali volatilization, closed-pore traps, and thermal-expansion-mismatch cracking as first-class failure modes.

---

### Composites Engineer
**Agent file:** `agents/composites-engineer.md`

Reasons from CLT/ABD laminate mechanics, Halpin–Tsai micromechanics, and CMH-17/NCAMP allowables through autoclave/OOA/RTM process control, ASTM D30 mechanical qualification, ultrasonic C-scan and CAI damage tolerance while treating fiber waviness, void content, under-cure, and quasi-isotropic strength traps as first-class failure modes.

---

### Corrosion Engineer
**Agent file:** `agents/corrosion-engineer.md`

Reasons from electrochemical couples, Pourbaix/galvanic selection, and ISO 15156 sour-service limits through AMPP SP0169/SP0502 CP and ECDA, CO₂ models (NORSOK M-506, OLI), coupon/ER/LPR monitoring, and ASTM G5/G48/G61 qualification while treating IR-masked CIPS, salt-spray overclaim, MIC vs. biocide residual, and MR0175≠fit-for-service as first-class failure modes.

---

### Crystal Growth Specialist
**Agent file:** `agents/crystal-growth-specialist.md`

Reasons from thermodynamic driving force, interface stability, constitutional supercooling, and dopant segregation (keff vs. k0, G/R) through Cz/Bridgman/FZ/LEC/PVT growth, CGSim and phase-field simulation, XRT topography, etch-pit counting, and FTIR/SIMS mapping while treating striations, inclusions, crucible-reaction contamination, and cool-down slip and cracking as first-class failure modes.

---

### Electronic Materials Engineer
**Agent file:** `agents/electronic-materials-engineer.md`

Reasons from band alignment, defect chemistry, and process–structure–property links; correlates Hall, C–V (Dit), XRD/RSM, SIMS, and ALD/MOCVD/sputtering recipes while treating dopant activation vs. chemical dose, high-κ trap charging, and reliability (NBTI/TDDB) as first-class failure modes.

---

### Energy Storage Battery Scientist
**Agent file:** `agents/energy-storage-battery-scientist.md`

Reasons from interfacial thermodynamics, ion transport, SEI/CEI dynamics, and cell engineering constraints (N/P and E/S ratio, mass loading) through galvanostatic cycling, dQ/dV, GITT and EIS/DRT, operando XRD, and PyBaMM/Newman models, while treating Li plating, lithium-inventory loss, transition-metal crossover, and coin-cell artifacts as first-class failure modes.

---

### Materials Physicist
**Agent file:** `agents/materials-physicist.md`

Reasons from band structure, defects, strain, and Landau order parameters; integrates HRXRD/RSM, ARPES, TEM/4D-STEM, van der Pauw transport, and SQUID/MOKE with Materials Project/VASP while treating matrix-element ARPES artifacts, substrate-dominated GIXRD, contact-resistance Hall errors, and DFT gap overclaim as first-class failure modes.

---

### Materials Scientist
**Agent file:** `agents/materials-scientist.md`

Reasons from CALPHAD phase diagrams, Scheil solidification, and Hall–Petch microstructure–property links; validates with XRD Rietveld QPA, EBSD, TEM/STEM, and ASTM mechanical testing while treating preferred orientation, FIB Ga artifacts, EBSD overlap, and Rietveld overfitting as first-class failure modes.

---

### Metallurgist
**Agent file:** `agents/metallurgist.md`

Reasons from phase diagrams, TTT/CCT paths, and Scheil solidification through Jominy hardenability (ASTM A255), ASM heat-treat cycles, metallography (ASTM E3/E112/E407), and staged failure analysis while treating decarburization, quench cracking, HAZ liquation, hot tearing, and microsegregation as first-class failure modes.

---

### Nanomaterials Scientist
**Agent file:** `agents/nanomaterials-scientist.md`

Reasons from size-dependent thermodynamics, surface-to-volume ratio, and DLVO colloidal stability through TEM/STEM statistics, DLS/NTA, XRD Scherrer, XPS, ICP-MS, and PL quantum-yield methods while treating aggregation, beam damage, intensity-weighted DLS sizing bias, and Ostwald ripening as first-class failure modes.

---

### Nanotechnologist
**Agent file:** `agents/nanotechnologist.md`

Reasons from length-scale manufacturing limits, EUV/NIL/EBL patterning, DSA defectivity, and interface-controlled integration through CD-SEM/AFM/TEM metrology, SEMI E10 yield discipline, and ISO 80004/FDA nanomaterial reporting while treating SEM shrinkage, NIL residual-layer non-uniformity, overlay error, and cherry-picked die yield as first-class failure modes.

---

### Optoelectronics Engineer
**Agent file:** `agents/optoelectronics-engineer.md`

Reasons from photon–electron conversion, ABC recombination, and IQE/EQE/WPE budgets; runs LIV/pulsed laser, EMVA 1288, and responsivity metrology; designs with Lumerical/Sentaurus/COMSOL TCAD and foundry PDKs while treating efficiency droop, thermal rollover, LIV kinks, and calibration geometry as first-class failure modes.

---

### Photonics Engineer
**Agent file:** `agents/photonics-engineer.md`

Reasons from Maxwell modes, FSR–Q–coupling trade-offs, and optical power/loss budgets; designs PICs and free-space systems with FDTD/INTERCONNECT/Zemax/GDSFactory and certifies links with OLTS/OTDR/M² while treating mesh dispersion errors, TE/TM birefringence, APC/PC connector mismatch, OTDR ghost/gainer events, and Fabry–Pérot convolution artifacts as first-class failure modes.

---

### Photovoltaics Solar Cell Scientist
**Agent file:** `agents/photovoltaics-solar-cell-scientist.md`

Reasons from the Shockley-Queisser detailed-balance limit and the diode coupling of Voc, Jsc, FF, and Rs/Rsh through light I-V, Suns-Voc implied Voc, EQE integration, lifetime mapping (QSSPC, μ-PCD, DLTS), and IEC 60904/61215 qualification while treating spectral mismatch, surface-recombination and shunt losses, perovskite hysteresis and ion migration, and PID/LID-LeTID degradation as first-class failure modes.

---

### Polymer Scientist
**Agent file:** `agents/polymer-scientist.md`

Reasons from molecular weight distribution, Tg/Tm and crystallinity, viscoelasticity, and phase behavior through GPC/SEC, DSC heat-cool-heat, capillary and oscillatory rheology, WAXD/SAXS, and DMA while treating thermal-history erasure, moisture hydrolysis, incomplete cure, and wrong-grade-lot artifacts as first-class failure modes.

---

### Renewable Energy Scientist
**Agent file:** `agents/renewable-energy-scientist.md`

Reasons from resource-to-energy conversion, P50/P90 yield risk, LCOE/LCA boundaries, IEC monitoring, and grid constraints while troubleshooting PV soiling/PID/clipping, wind wakes/icing/yaw, hydro drought, geothermal scaling, and biomass feedstock variability.

---

### Semiconductor Device Engineer
**Agent file:** `agents/semiconductor-device-engineer.md`

Reasons from electrostatics, capacitance-current MOSFET physics, interface-trap behavior, and self-heating through I-V/C-V extraction ladders, Sentaurus TCAD calibrated to silicon splits, BSIM-CMG compact modeling, and JEDEC reliability stress while treating uncalibrated TCAD, unstated constant-current Vt references, ignored BTI partial recovery, and self-heating-distorted DC Ron as first-class failure modes.

---

### Semiconductor Materials Scientist
**Agent file:** `agents/semiconductor-materials-scientist.md`

Reasons from band structure, defect energetics, and process–structure–property links; grows and characterizes bulk and epitaxial semiconductors (Si, III–V, SiC, GaN, 2D) via MOCVD/MBE/HVPE, Hall/DLTS/XRD/RSM/ECCI/TEM/SIMS, and DFT defect levels while treating compensation, Fermi-level pinning, threading dislocations, and polytype mixing as first-class failure modes.

---

### Superconductivity Scientist
**Agent file:** `agents/superconductivity-scientist.md`

Reasons from BCS/Eliashberg/GL order parameters, pairing symmetry, and vortex physics; validates Tc with Meissner/χ/C triads, phase-sensitive Josephson tests, ARPES/STM gaps, and EPW; uses SuperCon/3DSC and IEC 61788 Ic standards while treating filamentary transitions, pseudogap misreads, DAC flux trapping, and HTS quench detection gaps as first-class failure modes.

---

### Thin Film Scientist
**Agent file:** `agents/thin-film-scientist.md`

Reasons from nucleation and growth modes, film stress, interfacial adhesion, and conformality across topography through spectroscopic ellipsometry, XRR, Stoney wafer-curvature, XPS/RBS, and standards like ASTM E2244 and ISO 9211 while treating columnar porosity, barrier pinholes, reactive-sputter hysteresis drift, and uncalibrated-QCM thickness error as first-class failure modes.

---

### Tribologist
**Agent file:** `agents/tribologist.md`

Reasons from contact mechanics, lubricant rheology, Stribeck-regime and λ ratio through Hamrock-Dowson EHL film estimates, pin-on-disk/four-ball/SRV/FZG bench tests and SEM-EDS/ferrography scar analysis while treating scuffing, rolling-contact pitting, three-body abrasion and DLC adhesive transfer as first-class failure modes.

---

