# Engineering Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 90 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Engineering.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Acoustical Engineer
**Agent file:** `agents/acoustical-engineer.md`

Reasons from source-path-receiver control, logarithmic decibel levels, and mass-law transmission loss through IEC 61672 Class 1 metering, ISO 9613-2 propagation, SEA/FEM/BEM simulation, and ISO 9612 occupational surveys while treating flanking paths, coincidence dips, tonality penalties, and background-correction errors as first-class failure modes.

---

### Additive Manufacturing Engineer
**Agent file:** `agents/additive-manufacturing-engineer.md`

Reasons from melt-pool physics, VED, and thermal history through LPBF vs DED process selection, build orientation anisotropy, support design, powder lot control, CT/metallography NDE, and ASTM F42 / ISO-ASTM 529xx qualification—not generic 3D printing.

---

### Aerodynamicist
**Agent file:** `agents/aerodynamicist.md`

Reasons from circulation, Cp distributions, and boundary-layer physics through Re/Mach similitude, NACA airfoil polars, stall classification, wind-tunnel blockage/wall corrections, and SA/SST/LES external-aero CFD—not generic mechanical engineering.

---

### Aeronautical Engineer
**Agent file:** `agents/aeronautical-engineer.md`

Reasons from airfoil polars, drag buckets, and static margin through AVL/DATCOM stability derivatives, wind-tunnel blockage and wall corrections, FAR 25 §25.101–25.207 compliance matrices, and AC 25-7 flight-test evidence—not generic aerospace or pure CFD aerodynamics.

---

### Aerospace Engineer
**Agent file:** `agents/aerospace-engineer.md`

Reasons from margin-managed factors of safety, mass properties, and the analysis-test-similarity V&V hierarchy through FUN3D/SU2 CFD, NASTRAN/Abaqus FEA, JSBSim/Simulink 6-DOF, and FAR/CS, DO-178C, and NASA-STD compliance while treating flutter, buckling, inlet distortion, mass growth, and single-point failures as first-class failure modes.

---

### Antenna Engineer
**Agent file:** `agents/antenna-engineer.md`

Reasons from gain–directivity–efficiency, Chu–Harrington bandwidth limits, and array factor through HFSS/CST/FEKO synthesis, IEEE 149-2021 NF/FF/CATR metrology, CTIA TRP/TIS/ECC OTA, and Friis link budgets while treating ground-plane truncation, active impedance in arrays, range ripple, and S₁₁≠pattern conflation as first-class failure modes.

---

### Astrodynamicist
**Agent file:** `agents/astrodynamicist.md`

Reasons from two-body plus perturbation force models through Cowell/Encke propagation, batch LS and EKF orbit determination, SPICE/Horizons ephemerides, CCSDS OEM/CDM exchanges, and TEME–GCRF frame discipline while treating drag, stale TLE/B*, and covariance frame mismatch as first-class failure modes.

---

### Astronautical Engineer
**Agent file:** `agents/astronautical-engineer.md`

Reasons from the rocket equation, staging, and mass–power–Δv budgets through NPR 7120.5/ECSS-E-ST-10 subsystem specs, CEA/CEARUN and Sutton propulsion, CLA/pogo and TVAC I&T, GMAT/STK/SPICE mission design, CCSDS TM/TC link margins, and ADCS FDIR while treating unit/frame ICD mismatches, combustion instability, and MCO-class V&V gaps as first-class failure modes.

---

### Automotive Engineer
**Agent file:** `agents/automotive-engineer.md`

Reasons from vehicle-level requirements, regulatory limits, energy/exergy budgets, and distribution-based durability through DFMEA/DVP&R, DoE calibration (INCA, CANape, HIL), Pacejka tire and multibody models, rainflow fatigue, and source-path NVH analysis while treating undocumented build-level and cal-ID deltas, unmet emissions preconditioning and OBD readiness, ADAS sensor misalignment, and cross-domain torque-arbitration conflicts as first-class failure modes.

---

### Biomedical Engineer
**Agent file:** `agents/biomedical-engineer.md`

Reasons from ISO 14971 risk management, ISO 10993 biocompatibility matrices, ASTM F/ISO 14242 mechanical and wear testing, and FDA 510(k) substantial equivalence; treats stress shielding, UHMWPE osteolysis, F2129 corrosion artifacts, and predicate/material mismatches as first-class failure modes.

---

### Bioprocess Engineer
**Agent file:** `agents/bioprocess-engineer.md`

Reasons from QTPP–CPP–CQA QbD, CHO fed-batch/perfusion scale-up (P/V, kLa, mixing), platform mAb DSP (Protein A, low-pH viral hold, IEX polish, UF/DF), tech transfer and PPQ lifecycle; treats transport-limited scale-up, harvest fouling, on-column aggregation, SUB leachables, and arbitrary three-batch PPQ as first-class failure modes.

---

### Brain Computer Interface Engineer
**Agent file:** `agents/brain-computer-interface-engineer.md`

Reasons from modality–paradigm fit (EEG, ECoG, Utah arrays), CSP/Riemannian decoding (pyriemann, MOABB), BCI2000/OpenBCI pipelines, and charge-density stimulation safety; validates within- vs cross-session claims and treats muscle ICA, impedance drift, and IDE/IRB gates as first-class failure modes.

---

### Bridge Engineer
**Agent file:** `agents/bridge-engineer.md`

Reasons from load paths, limit states, redundancy, and durability through AASHTO LRFD rating (LRFR/inventory vs. operating), FEM grillage and OpenSees models, HEC-18 scour analysis, and NDE such as half-cell potential and phased-array UT while treating fracture-critical fatigue details, lost composite action, scour, and bearing seizure as first-class failure modes.

---

### Building Science Engineer
**Agent file:** `agents/building-science-engineer.md`

Reasons from coupled heat-air-moisture transport through ASHRAE 160 moisture-design analysis, WUFI transient simulation, ACH50 leakage mapping, and ISO 10211 psi-values while treating exfiltration condensation, reservoir claddings, and mold-index sensitivity as first-class failure modes.

---

### Catalysis Engineer
**Agent file:** `agents/catalysis-engineer.md`

Reasons from catalyst lifecycle margin, space velocity (WHSV/GHSV/LHSV), and deactivation economics through plant historian trends, MAT/pilot trickle-bed activity tests, Aspen HYSYS activity factors, and ASTM crush/attrition plus TPO/ICP spent-catalyst profiling while treating coke, poisoning, sintering, attrition, and channeling/maldistribution as first-class failure modes.

---

### Chemical Engineer
**Agent file:** `agents/chemical-engineer.md`

Reasons from closing mass, energy, and momentum balances and competing equilibrium/kinetics/transport regimes through Aspen Plus/HYSYS flowsheeting, McCabe-Thiele and Damkohler-based sizing, pinch analysis, and HAZOP/LOPA with API 520/521 relief, while treating azeotrope-pinched columns, reactor runaway, recycle impurity accumulation, and pump cavitation (NPSHa<NPSHr) as first-class failure modes.

---

### Civil Engineer
**Agent file:** `agents/civil-engineer.md`

Reasons from load paths, factored load combinations, soil-structure interaction, and governing limit states through ASCE 7, ACI 318, AISC 360, and tools like SAP2000/ETABS, PLAXIS, and HEC-RAS while treating missing load paths, connection and foundation failures, differential settlement, and unvalidated FEA as first-class failure modes.

---

### Coastal Engineer
**Agent file:** `agents/coastal-engineer.md`

Reasons from joint-probability surge and waves through CEM/EurOtop runup-overtopping, Van der Meer/Rock Manual armor, CERC–Van Rijn sediment budgets, and CMS/XBeach/ADCIRC–SWAN model selection while treating toe scour, armor breakage, datum mismatch (BFE vs MHHW), and downdrift impacts as first-class failure modes.

---

### Combustion Engineer
**Agent file:** `agents/combustion-engineer.md`

Reasons from stoichiometry, flame stability, emissions, and CFD-reacted flows while treating blow-off, flashback, and soot formation as first-class failure modes.

---

### Communications Engineer
**Agent file:** `agents/communications-engineer.md`

Reasons from Shannon capacity and matched-filter detection through OFDM/MIMO, 3GPP NR LDPC/polar (TS 38.212), TR 38.901 link budgets, Keysight 89600 VSA EVM, ns-3 SLS, and berconfint Monte Carlo while treating CFO/IQ/phase-noise coupling, pre- vs post-FEC BER, and AWGN-only optimism as first-class failure modes.

---

### Computer Hardware Engineer
**Agent file:** `agents/computer-hardware-engineer.md`

Reasons from CPI/AMAT and MESI/MOESI coherence through SystemVerilog RTL, PrimeTime/Design Compiler/Innovus signoff, PCIe LTSSM/TLP, SVA formal, and clock-gating power while treating CDC metastability, false-path abuse, X-optimism, and coherency traffic as first-class failure modes.

---

### Construction Engineer
**Agent file:** `agents/construction-engineer.md`

Reasons from design intent versus means-and-methods through CPM/P6 and Last Planner scheduling, Revit/Navisworks BIM coordination, IBC Chapter 17 special inspections, ASTM C31/C39 cylinder acceptance, and ACI 318 low-break/core protocols while treating formwork collapse, honeycombing, tolerance stack-up, and schedule logic errors as first-class failure modes.

---

### Control Systems Engineer
**Agent file:** `agents/control-systems-engineer.md`

Reasons from plant dynamics, stability margins, and disturbance-rejection specs through Bode/Nyquist and Routh-Hurwitz analysis, LQR/H-infinity and pole placement, Kalman/EKF observers, RGA pairing, and HIL validation while treating integrator windup, actuator saturation and backlash limit cycles, sensor delay masking phase margin, and estimator divergence as first-class failure modes.

---

### Cryptography Engineer
**Agent file:** `agents/cryptography-engineer.md`

Reasons from explicit threat models, vetted primitives, key hierarchy, and constant-time secret handling through STRIDE threat modeling, standards (RFC 8446 TLS 1.3, FIPS 203/204, Ed25519), test vectors (Wycheproof, NIST CAVP), and protocol verifiers (Tamarin, ProVerif) while treating nonce reuse in AEAD, padding/Bleichenbacher oracles, timing side channels, and weak-RNG keys as first-class failure modes.

---

### Earthquake Engineer
**Agent file:** `agents/earthquake-engineer.md`

Reasons from ASCE 7 DRS and SDC, capacity design (R, Cd, Ω₀), ELF/MRS/NRHA and ASCE 41 pushover; models in SAP2000/ETABS/OpenSees with PEER NGA-West2 motions; treats liquefaction, soft-story P-delta collapse, and record-scaling artifacts as first-class failure modes.

---

### Electric Machines Engineer
**Agent file:** `agents/electric-machines-engineer.md`

Reasons from magnetic circuit design, dq-frame machine models, FEM flux paths, and drive efficiency maps while treating saturation, cogging, thermal derating, and inverter harmonics as first-class failure modes.

---

### Electrical Engineer
**Agent file:** `agents/electrical-engineer.md`

Reasons from Kirchhoff's laws, Maxwell's quasi-static limit, energy conservation, and LTI superposition through SPICE loop-gain and corner analysis, Bode gain/phase-margin checks, impedance-controlled layout, and IEC 62368/CISPR compliance, while treating unmodeled PCB parasitics, ground-return loops, protection let-through energy versus semiconductor SOA, and probe-artifact confounders as first-class failure modes.

---

### Electromagnetics Engineer
**Agent file:** `agents/electromagnetics-engineer.md`

Reasons from Maxwell scaling and S-parameters through HFSS/CST/ADS workflows, SOLT/TRL calibration, mesh ΔS convergence, Smith-chart matching, anechoic OTA, and CISPR/FCC Part 15 / IEC-IEEE 62209-1528 SAR compliance while treating PML reflections, probe de-embedding, and chamber ripple as first-class failure modes.

---

### Electronics Engineer
**Agent file:** `agents/electronics-engineer.md`

Reasons from datasheet-corner device physics, signal-chain error budgets, and analog-digital return-path coupling through LTspice/IBIS-AMI simulation, ICT/boundary-scan coverage, golden-board signature comparison, and IPC/AEC-Q standards while treating ESD versus EOS overstress, MLCC DC-bias derating, reference and clock-jitter ENOB loss, and NFF field returns as first-class failure modes.

---

### Embedded Systems Engineer
**Agent file:** `agents/embedded-systems-engineer.md`

Reasons from hardware timing, interrupt latency, memory maps, and deterministic WCET resource bounds through DWT CYCCNT and Saleae logic-analyzer timing proofs, SWD/JTAG (J-Link/OpenOCD) with CFSR/HFSR/BFAR fault decode, FreeRTOS/Zephyr respecting configMAX_SYSCALL_INTERRUPT_PRIORITY, MISRA C:2012 and ISO 26262 ASIL discipline, Nordic PPK2 power profiling, and MCUboot signed OTA while treating priority inversion, Cortex-M7 uncached-DMA D-cache incoherence, CAN bus-off, I2C NACK storms, and brownout-during-flash-write NVS corruption as first-class failure modes.

---

### Energy Systems Engineer
**Agent file:** `agents/energy-systems-engineer.md`

Reasons from exergy, load duration curves, capacity factor, and grid boundary constraints through pinch analysis, hourly dispatch models (PLEXOS, HOMER Pro, SAM, PVsyst), spark-spread CHP screening, and IPMVP M&V while treating nameplate-vs-utilization confusion, average-vs-marginal grid emissions, unrealistic arbitrage spreads, and demand-charge ratchet resets as first-class failure modes.

---

### Environmental Engineer
**Agent file:** `agents/environmental-engineer.md`

Reasons from mass balances, reaction kinetics, source-pathway-receptor transport, and permit limits through BioWin/GPS-X, SWMM, AERMOD/CALPUFF, GAC/IX and activated-sludge design, and 40 CFR Part 136 QA/QC, while treating nitrifier washout, clarifier upset, PFAS breakthrough, and remediation rebound as first-class failure modes.

---

### Finite Element Analyst
**Agent file:** `agents/finite-element-analyst.md`

Reasons from discretization error, element technology, and constraint physics; runs mesh convergence and Richardson studies, Nastran/Abaqus/ANSYS workflows, RBE2/RBE3 and contact discipline, and ASME V&V 10 verification-before-validation reporting on governing QoIs.

---

### Fire Protection Engineer
**Agent file:** `agents/fire-protection-engineer.md`

Reasons from NFPA 13 Hazen-Williams hydraulics (K-factor, remote area, hose stream) and NFPA 101 egress (occupant load, travel distance, capacity factors) through NFPA 92 smoke containment/management, ASET/RSET PBD, and FDS/CFAST/CONTAM/PyroSim modeling while treating breached compartmentation, C-factor/fitting errors, and supply-curve shortfall as first-class failure modes.

---

### Fluid Mechanics Engineer
**Agent file:** `agents/fluid-mechanics-engineer.md`

Reasons from Navier–Stokes reductions through Darcy–Weisbach/Crane TP-410 pipe networks, pump system curves, NPSH/affinity laws, HI turbomachinery selection, and ASME V&V 20 CFD validation when simulation supports design.

---

### Foundation Engineer
**Agent file:** `agents/foundation-engineer.md`

Reasons from effective stress, ULS versus SLS limit states, and construction-altered soil behavior through CPT/SPT logging, triaxial and oedometer testing, LRFD φ-factor checks, and LPILE/PLAXIS analysis while treating liquefaction-driven lateral spread, negative skin friction downdrag, differential settlement, and scour as first-class failure modes.

---

### Fpga Engineer
**Agent file:** `agents/fpga-engineer.md`

Reasons from metastability budgets, setup/hold margins, and tool-reported WNS/TNS through Vivado/Quartus timing and CDC reports, XDC/SDC constraints, Spyglass/Verilator lint, and ILA/IBERT lab bring-up while treating unsafe clock-domain crossings, reset domain crossings, sim-versus-silicon X mismatches, and unconstrained timing paths as first-class failure modes.

---

### Geotechnical Engineer
**Agent file:** `agents/geotechnical-engineer.md`

Reasons from effective stress and LRFD/EC7 limit states through GDR/GBR/FDR deliverables, shallow and deep foundations (GEC 6/10/12), excavation support (DeepEX, LPILE), ground improvement, ASCE 7 liquefaction, observational-method triggers, and FHWA pile acceptance while treating DSC claims, setup vs. blow count, and GBR-vs-design conflation as first-class failure modes.

---

### Heat Transfer Engineer
**Agent file:** `agents/heat-transfer-engineer.md`

Reasons from conduction, convection, radiation, and coupled fluid-solid physics through thermal resistance networks, Biot/NTU/film-temperature scaling, LMTD and epsilon-NTU exchanger methods, fin efficiency, and conjugate-heat-transfer CFD while treating contact resistance and TIM pump-out, fouling, boiling CHF, non-condensables, and non-conservative interface flux mapping as first-class failure modes.

---

### Hvac Engineer
**Agent file:** `agents/hvac-engineer.md`

Reasons from psychrometric state, parallel heating and cooling load paths, and vapor-compression thermodynamics through TRACE/HAP and EnergyPlus load models, ASHRAE 62.1/55/90.1 and Guideline 36 sequences, and TAB/commissioning per ASHRAE 15/34, while treating low ΔT syndrome, simultaneous reheat fight, coil-leaving condensation, and A2L refrigerant safety as first-class failure modes.

---

### Hydraulic Engineer
**Agent file:** `agents/hydraulic-engineer.md`

Reasons from Bernoulli–Darcy–Weisbach, Moody diagrams, HEC-RAS/EPANET modeling, and pump/system curves while treating transient water hammer, air entrainment, and roughness aging as first-class failure modes.

---

### Industrial Engineer
**Agent file:** `agents/industrial-engineer.md`

Reasons from takt, Little's Law, and ρ-stable queueing (M/M/c, Erlang C) through DMAIC/DMADV, VSM, line balancing, SLP/ALDEP/CRAFT layout, MTM/MOST, work sampling, RNLE/RULA/REBA, ISO 22400 OEE, and Arena/AnyLogic DES V&V; treats simulation warm-up/replication gaps, CRAFT non-contiguity, and OEE-without-takt red herrings as first-class failure modes.

---

### Instrumentation Engineer
**Agent file:** `agents/instrumentation-engineer.md`

Reasons from the process variable, its transduction chain, 4-20 mA loop integrity, and traceable calibration through ISA-5.1 P&IDs, NAMUR NE43 fault bands, ISO 5167 orifice sizing, and GUM uncertainty budgets while treating plugged impulse lines, double-applied square-root, ground-loop noise, and unrevalidated SIS bypasses as first-class failure modes.

---

### Integrated Circuit Designer
**Agent file:** `agents/integrated-circuit-designer.md`

Reasons from spec through Virtuoso schematic/layout, Calibre DRC/LVS/RCX, and foundry PDK corners across analog, mixed-signal, RF, and structured digital blocks; treats TT-only signoff, LVS-without-PEX, and common-centroid violations as first-class tapeout failure modes.

---

### Manufacturing Engineer
**Agent file:** `agents/manufacturing-engineer.md`

Reasons from process physics, capability, and cost through Shercliff-Lovatt process selection, ASME Y14.5 GD&T, CAM simulation, and AIAG APQP/PPAP with MSA-gated SPC capability, treating high %GRR masquerading as variation, false Cpk on unstable or short runs, datum-scheme mismatch, and uncontrolled ECN tweaks as first-class failure modes.

---

### Marine Engineer
**Agent file:** `agents/marine-engineer.md`

Reasons from propulsion thermodynamics, shaft BPF/torsional barred speeds, central LT/HT cooling, class machinery surveys, and ISO 15016:2025 sea trials while treating cat fines liner wear, scavenge fire, purifier mis-set, blackout PMS logic, and tropical SW fouling as first-class failure modes.

---

### Mechanical Design Engineer
**Agent file:** `agents/mechanical-design-engineer.md`

Reasons from function, datum reference frames, and tolerance budgets; releases inspectable drawings and MBD through ASME Y14.5 GD&T, WC/RSS/Monte Carlo stack-ups, SAE J1739 DFMEA (Action Priority), and Boothroyd–Dewhurst DFM/DFA—not stress plots alone.

---

### Mechanical Engineer
**Agent file:** `agents/mechanical-engineer.md`

Reasons from equilibrium, failure physics, and code-backed allowables; designs through requirements, GD&T, DFMEA, and hand/FEA/test validation with explicit governing failure modes.

---

### Mechatronics Engineer
**Agent file:** `agents/mechatronics-engineer.md`

Reasons from reflected inertia, control bandwidth, sensor physics, and thermal duty cycle through Bode loop-shaping with phase/gain margins, FOC current-velocity-position loops, plant identification, HIL, and IEC 61800-5-2 STO architecture while treating backlash and structural-mode resonance, transport-delay phase loss, encoder aliasing, and EMC ground loops as first-class failure modes.

---

### Mems Engineer
**Agent file:** `agents/mems-engineer.md`

Reasons from scale-dependent mechanics, squeeze-film damping, and electrostatic pull-in through DRIE Bosch/surface micromachining, CoventorMP/COMSOL, foundry PDKs, LDV/WLI metrology, and AEC-Q103 qual while treating release stiction, DRIE scallop bias, package-stress offset drift, and functional-WLT-vs-reliability gaps as first-class failure modes.

---

### Microelectronics Engineer
**Agent file:** `agents/microelectronics-engineer.md`

Reasons from CTE mismatch, θja networks (JESD51), and package RLC through wire bond (Au–Al IMC, loop height), flip-chip (UBM, underfill, HIP/NWO), J-STD-020 MSL, and JESD22 TCT/uHAST; treats datasheet θja without board definition, wire sweep, die-attach voids, and soak-mode mismatch as first-class failure modes.

---

### Naval Architect
**Agent file:** `agents/naval-architect.md`

Reasons from displacement, Bonjean/KN–GZ stability, ITTC-78 resistance extrapolation, Wageningen B-series propulsion, WAMIT/NEMOH seakeeping, and IACS CSR scantlings while treating Froude/Re scale mismatch, free-surface GM error, Holtrop range violations, and trial CA bias as first-class failure modes.

---

### Network Engineer
**Agent file:** `agents/network-engineer.md`

Reasons from OSI layering, control vs. data plane, and path symmetry through BGP policy (TCP/179, communities, RR), OSPF areas/LSA adjacency, 802.1Q VLAN/trunk design, spine-leaf Clos/VXLAN-EVPN fabrics, and L1→L7 troubleshooting while treating asymmetric routing, MTU black holes, native-VLAN mismatch, and BGP OutQ/hold-time flaps as first-class failure modes.

---

### Neuroengineer
**Agent file:** `agents/neuroengineer.md`

Reasons from electrode–electrolyte charge-density limits and foreign-body gliosis through Utah/Neuropixels chronic recording, EIS impedance spectroscopy, Kilosort3/MountainSort validation, FDA IDE pathways, and explant histology (GFAP/Iba1) while treating impedance drift, unvalidated auto-sort inflation, and acute-to-chronic yield collapse as first-class failure modes.

---

### Nuclear Engineer
**Agent file:** `agents/nuclear-engineer.md`

Reasons from k_eff, DNBR/CHF margins, xenon transients, and defense-in-depth; couples SCALE/MCNP, PARCS, TRACE/RELAP, and MELCOR to 10 CFR and PRA; treats nodalization, nuclear-data, and CHF-correlation uncertainties as first-class failure modes.

---

### Pavement Engineer
**Agent file:** `agents/pavement-engineer.md`

Reasons from layered-elastic stress/strain, traffic spectra, climate, and material temperature-dependence through AASHTOWare Pavement ME (MEPDG) hierarchical inputs, FWD deflection-basin backcalculation with GPR/core thickness, binder PG selection, and LTPP-calibrated transfer functions, while treating mis-specified traffic, seasonal moisture-weakened subgrade, reflective cracking, and construction segregation as first-class failure modes.

---

### Petroleum Reservoir Engineer
**Agent file:** `agents/petroleum-reservoir-engineer.md`

Reasons from Darcy flow, Havlena–Odeh MBE, Fetkovich/VEH aquifers, Horner/derivative PTA, Buckley–Leverett/Welge floods, Eclipse/CMG/tNavigator history match, PRMS/SEC reserves (P90/P50/P10), and SPE11 CO₂ benchmarks; treats transient Arps b>1, negative-skin grid artifacts, and microseismic≠SRV as first-class failure modes.

---

### Pollution Control Engineer
**Agent file:** `agents/pollution-control-engineer.md`

Reasons from PTE, Title V Part 70, and NPDES limits through scrubber/baghouse/ESP/RTO selection, CEMS and stack-test demonstration, and parametric O&M (ΔP, pH, L/G) while treating synthetic-minor strategy, sulfite-blinded FGD, bag leaks, and WET/TIE toxicity as first-class failure modes.

---

### Power Electronics Engineer
**Agent file:** `agents/power-electronics-engineer.md`

Reasons from volt-second and charge balance, switched-mode energy transfer, and small-signal loop gain through PLECS/LTspice/SIMPLIS simulation, Steinmetz and Dowell magnetics loss accounting, Bode injection on hardware, and LISN-based EMI scans while treating shoot-through, RHP-zero subharmonic oscillation, Qrr and ZVS-window loss, and CM-choke saturation as first-class failure modes.

---

### Power Grid Engineer
**Agent file:** `agents/power-grid-engineer.md`

Reasons from AC power flow, N-1 contingency, and relay coordination through PSS/E studies, distance/differential protection, IBR/IEEE 2800 models, COMTRADE event analysis, and NERC TPL/PRC standards while treating EMS topology drift, voltage collapse, and ATC vs nameplate as first-class failure modes.

---

### Power Systems Engineer
**Agent file:** `agents/power-systems-engineer.md`

Reasons from per-unit impedances, symmetrical components, swing equations, and relay reach through PSS/E, OpenDSS, Aspen OneLiner, PSCAD, and NERC TPL/IEEE 1547/IEC 60909 criteria while treating loss of protection selectivity, DER-driven reverse power flow and voltage rise, CT saturation, and voltage collapse as first-class failure modes.

---

### Precision Engineering Specialist
**Agent file:** `agents/precision-engineering-specialist.md`

Reasons from ASME Y14.5 GD&T, GUM uncertainty, and micrometer error budgets through CMM programming (ISO 10360), volumetric compensation, UPDT/STS diamond turning, and ISO 14253 decision rules while treating datum mis-simulation, MMC bonus omission, and CMM program drift as first-class failure modes.

---

### Process Engineer
**Agent file:** `agents/process-engineer.md`

Reasons from conservation laws, CSTR/PFR selectivity and RTD/Da scale-up through BFD→PFD→P&ID/HAZOP/LOPA/SIL, Aspen Plus/HYSYS HMB, API 520/521 relief and LMTD/F_t exchanger sizing, and lab→pilot→plant commissioning while treating frozen-design violations, simulation-without-data, and BPCS/IPL conflation as first-class failure modes.

---

### Propulsion Engineer
**Agent file:** `agents/propulsion-engineer.md`

Reasons from thrust, specific impulse, characteristic velocity c*, thrust coefficient Cf, and NPSH through NASA CEA, RPA and NPSS cycle models, hot-fire thrust stands, and ROCCID/bomb-test stability screening while treating nozzle separation, inducer cavitation, chugging/screech combustion instability, and scramjet unstart as first-class failure modes.

---

### Quality Six Sigma Engineer
**Agent file:** `agents/quality-six-sigma-engineer.md`

Reasons from process variation, defect operational definitions, and customer-critical characteristics through Shewhart control charts, Gage R&R (%GRR, ndc), Cp/Cpk and Pp/Ppk capability, DMAIC tollgates, and AIAG PPAP/PFMEA in Minitab or JMP while treating Cpk on unstable processes, attribute data forced as normal, gauge spread consuming tolerance, and unverified projected savings as first-class failure modes.

---

### Reaction Engineering Specialist
**Agent file:** `agents/reaction-engineering-specialist.md`

Reasons from rate laws, stoichiometry, residence-time distributions, and coupled heat-rate balances through LHHW and Michaelis-Menten kinetics, Thiele/effectiveness and Weisz-Prater diffusion criteria, tracer RTD models, and RC1/ARC calorimetry while treating thermal runaway, hot spots, catalyst deactivation, channeling, and k_L-a mass-transfer masking as first-class failure modes.

---

### Reliability Engineer
**Agent file:** `agents/reliability-engineer.md`

Reasons from failure mechanisms, time-to-failure distributions, censored field data, and stress-strength interference through FMECA, physics-of-failure models (Coffin-Manson, Arrhenius, Peck), Weibull and Crow-AMSAA growth analysis, and demonstration tests while treating mixture populations, wrong acceleration models, common-cause failures, and lab-pass-equals-field-proof as first-class failure modes.

---

### Rf Microwave Engineer
**Agent file:** `agents/rf-microwave-engineer.md`

Reasons from power-wave S-parameters, Friis noise-figure cascades, and Rollett/mu stability through ADS/AWR harmonic balance, HFSS/Sonnet EM, Smith-chart matching, and TRL/SOLT-calibrated VNA/spectrum bench work while treating reference-plane errors, LO leakage and IF feedthrough, conditional instability, and uncorrelated sim-versus-measured gain as first-class failure modes.

---

### Robotics Engineer
**Agent file:** `agents/robotics-engineer.md`

Reasons from DH/PoE kinematics, Jacobian singularities, and computed-torque/impedance control through ROS 2, MoveIt/OMPL, Nav2/SLAM/AMCL, hand-eye AX=XB, Isaac/Gazebo sim-to-real, and ISO 10218/ISO TS 15066 safety while treating tf/frame errors, encoder drift, backlash, and reality-gap overclaim as first-class failure modes.

---

### Robotics Scientist
**Agent file:** `agents/robotics-scientist.md`

Reasons from the closed sensor-to-actuator loop, kinematic reachability, and dynamic feasibility (friction cones, actuator saturation) through DH/PoE kinematics, RRT*/CHOMP planning, MPC and whole-body control, SLAM, and ROS 2 rosbag logging while treating TF-frame and timestamp mismatches, the sim-to-real gap, grasp slip, and ISO 10218/15066 force-limit violations as first-class failure modes.

---

### Sensor Engineer
**Agent file:** `agents/sensor-engineer.md`

Reasons from transduction physics and error budgets through MEMS IMU Allan variance (ARW, bias instability, rate random walk), six-position and temperature calibration, piezoresistive/capacitive pressure validation, and photodiode–TIA NEP/SNR while treating vibration rectification, mag distortion, and aliased decimation as first-class failure modes.

---

### Separation Processes Engineer
**Agent file:** `agents/separation-processes-engineer.md`

Reasons from VLE/LLE thermodynamics, FUG shortcuts, and NRTL/PR property packages through Aspen RadFrac, CGCC/pinch integration, membrane Robeson bounds, chromatography van Deemter scale-up, and MSZW crystallization while treating wrong BIPs, jet flood/entrainment, concentration polarization, and lab-to-plant MSZW as first-class failure modes.

---

### Signal Processing Engineer
**Agent file:** `agents/signal-processing-engineer.md`

Reasons from the sampling theorem, LTI system functions H(z), and sufficient statistics for detection through Parks-McClellan filter design, Welch and multitaper spectral estimation, matched filters and CFAR detection, and bit-true fixed-point verification while treating aliasing, leakage and scalloping, IIR limit cycles, and detector leakage as first-class failure modes.

---

### Structural Engineer
**Agent file:** `agents/structural-engineer.md`

Reasons from equilibrium, load-path continuity, ductility, and code-mandated safety formats through ASCE 7 load combinations, ETABS/SAP2000 models with independent hand checks, AISC 360/341 and ACI 318 capacity design, and ASCE 41 evaluation, while treating soft-story drift, brittle connection and anchor breakout failures, neglected serviceability, and progressive collapse as first-class failure modes.

---

### Surface Engineering Specialist
**Agent file:** `agents/surface-engineering-specialist.md`

Reasons from tribological system design, Archard wear, Stribeck regimes, and Pourbaix/galvanic coupling; selects PVD/CVD/PEO/conversion stacks with HiPIMS etch and interlayers; validates with ISO 20502 scratch, ASTM G99/G133, G119 tribocorrosion, and ISO 14577 nanoindentation while treating delamination stress, arc macroparticles, pinhole galvanics, and cross-cut misuse on hard films as first-class failure modes.

---

### Surveyor Geomatics Engineer
**Agent file:** `agents/surveyor-geomatics-engineer.md`

Reasons from datum/epoch/geoid and NSRS 2022 migration, CSF grid–ground, Baarda/3D least squares, NGS 92/ALTA RPP/ASPRS RMSE and IHO S-44 TPU; treats prism constants, BIM Helmert, and mixed CRS as first-class failure modes.

---

### Systems Engineer
**Agent file:** `agents/systems-engineer.md`

Reasons from stakeholder needs, ISO/IEC/IEEE 15288 life-cycle processes, and V-model verification/validation through bidirectional requirements trace (DOORS/Polarion), MBSE SysML digital threads, ICD interface control, DSM integration sequencing, MCDA trade studies, and FMEA/FTA/STPA risk—while treating scope creep, gold plating, traceability gaps, and ICD mismatches as first-class failure modes.

---

### Telecommunications Engineer
**Agent file:** `agents/telecommunications-engineer.md`

Reasons from Shannon–Hartley capacity (C = B log2(1+S/N)), dB link-budget accounting, and FSPL-plus-ITU-R propagation physics through 3GPP Rel-15/16/17 NR PHY and 5G numerology (15/30/60/120 kHz SCS), IEEE 802.11ax/6E air interfaces, ITU-R P.1546/P.1812/P.452 planning, TS 38.141 test models with VSA EVM/ACLR, IEC 62037 two-tone PIM, and Y.1731/Y.1564 Ethernet OAM while treating passive intermodulation, co-channel/adjacent-channel interference, backhaul GTP bottlenecks masquerading as air-interface failure, and IEEE 1588v2/GPS sync loss as first-class failure modes.

---

### Thermodynamics Engineer
**Agent file:** `agents/thermodynamics-engineer.md`

Reasons from energy conservation, entropy generation, state properties, and exergy quality through cycle modeling on T-s/h-s diagrams, IAPWS-IF97/REFPROP/CoolProp property models, LMTD/ε-NTU and pinch analysis, and ASME PTC/AHRI acceptance protocols, while treating efficiency-above-Carnot claims, pinch violations, compressor surge, and inconsistent HHV/LHV bases as first-class failure modes.

---

### Traffic Engineer
**Agent file:** `agents/traffic-engineer.md`

Reasons from LWR/CTM flow, HCM delay/v/c/LOS, K-D-PHF-DDHV volumes, ITE TGM 12th/MTIASD TIAs, Synchro/HCS/SIDRA/VISSIM workflows, and HSM SPF+CMF+EB safety — treating unc calibrated models, naive before–after crashes, and LOS-without-v/c as first-class failure modes.

---

### Transportation Engineer
**Agent file:** `agents/transportation-engineer.md`

Reasons from four-step and activity-based travel demand (CUBE/Visum/EMME), AASHTO Green Book geometry, HCM capacity, MPO LRTP and NEPA 23 CFR 771 project development, and multimodal corridor MOEs while treating unvalidated TDM forecasts and capacity-without-demand balance as first-class failure modes.

---

### Tunnel Underground Engineer
**Agent file:** `agents/tunnel-underground-engineer.md`

Reasons from ground-structure-water-air interaction, convergence-support interaction, and face-stability limit states through Q/RMR/GSI classification, Hoek-Brown numerical models (PLAXIS, FLAC), Peck settlement troughs, and DAUB-ITA/NFPA 502 standards while treating face blowout, squeezing, invert heave, and TBM jam in mixed face as first-class failure modes.

---

### Turbomachinery Engineer
**Agent file:** `agents/turbomachinery-engineer.md`

Reasons from Euler work transfer, velocity triangles, decomposed loss correlations, and map-based off-design margin through meanline-to-throughflow-to-RANS/URANS analysis, Campbell and unbalance rotordynamics, and ASME PTC 10/PTC 6 and API 617 testing while treating surge and rotating stall, clearance rubs and tip leakage, pump cavitation below NPSHr, and seal cross-coupling instability as first-class failure modes.

---

### Urban Infrastructure Planner
**Agent file:** `agents/urban-infrastructure-planner.md`

Reasons from comp plan–FLUM–zoning consistency through Euclidean/form-based overlays, CIP/TIP–STIP and ISO 55001/IIMM asset portfolios, ArcGIS Urban parcel workflows, and CEJST/AFFH/Justice40 equity screening while treating FLUM–zoning mismatch, CRS topology errors, and unfunded backlog as first-class failure modes.

---

### Vacuum Science Technology Engineer
**Agent file:** `agents/vacuum-science-technology-engineer.md`

Reasons from molecular flux (P = n k_B T), conductance-limited effective pumping speed, and surface outgassing through He mass-spectrometer leak detection, rate-of-rise tests, RGA fingerprinting, and Molflow+ conductance modeling while treating virtual leaks, H₂ permeation, ion-gauge contamination, and hydrocarbon backstreaming as first-class failure modes.

---

### Vibration Dynamics Engineer
**Agent file:** `agents/vibration-dynamics-engineer.md`

Reasons from FRF/coherence, MAC, and damping identification through impact/shaker EMA, spectral ODS, FFT windowing, Campbell/critical-speed rotordynamics, and ISO 20816/API 610 diagnostics while treating double-hit, mass-loading, ODS–mode conflation, oil whirl/whip, and leakage as first-class failure modes.

---

### Vlsi Chip Design Engineer
**Agent file:** `agents/vlsi-chip-design-engineer.md`

Reasons from PPA tradeoffs, timing slack, on-chip variation, and foundry rule decks through MCMM STA with OCV/POCV in PrimeTime/Tempus, UPF power intent, SpyGlass/JasperGold CDC, and Calibre DRC/LVS while treating clock-domain crossings, post-CTS hold violations, IR drop, and TT-only signoff as first-class failure modes.

---

### Water Resources Engineer
**Agent file:** `agents/water-resources-engineer.md`

Watershed hydrology through HEC-HMS into HEC-RAS floodplain and stormwater BMP design — catchment balance, DSS coupling, FEMA products, and quantity/quality detention with defensible calibration.

---

### Welding Joining Engineer
**Agent file:** `agents/welding-joining-engineer.md`

Reasons from heat input, t8/5, HAZ metallurgy, and restraint/shrinkage through AWS D1.1 prequalified vs qualified WPS, ASME IX/ISO 15614 PQR essential variables, RT/UT acceptance (static vs cyclic), FSW wormhole/kissing-bond windows, and neutron/XRD/hole-drilling residual stress while treating prequalification overreach, planar-UT mis-disposition, and cold-FSW root bonds as first-class failure modes.

---

### Wind Engineering Specialist
**Agent file:** `agents/wind-engineering-specialist.md`

Reasons from ABL exposure, ASCE 7-22/EN 1991-1-4 wind actions, ASCE 49 BLWT Method 3, rigid vs flexible G/Gf, MWFRS vs C&C, and DAD directionality; treats enclosure GCpi, short-fetch exposure, and aeronautical-tunnel misuse as first-class failure modes.

---

