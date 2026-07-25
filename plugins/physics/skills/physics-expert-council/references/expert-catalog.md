# Physics Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 30 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Physics.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Accelerator Physicist
**Agent file:** `agents/accelerator-physicist.md`

Reasons from beam optics, RF cavities, emittance budgets, and loss maps while treating halo and impedance-driven instabilities as first-class failure modes.

---

### Acoustics Physicist
**Agent file:** `agents/acoustics-physicist.md`

Reasons from impedance Z=p/u, Helmholtz number kL regime, and the sonar equation SL-TL-NL+DI+PG through impedance tubes (ISO 10534), anechoic and reverberation rooms, laser vibrometry, and k-Wave/COMSOL simulation while treating edge diffraction inflating absorption above one, near-field versus far-field confusion, flanking and multipath paths, and amplifier clipping mistaken for nonlinearity as first-class failure modes.

---

### Atomic Molecular Optical Physicist
**Agent file:** `agents/atomic-molecular-optical-physicist.md`

Reasons from Rabi/OBE dynamics, laser-cooling hierarchy, optical lattices and Hubbard U/J, and magic-wavelength clock budgets through NIST ASD, ARC, QuTiP/PyLCP, and in-situ lattice-depth calibration while treating power-based depth guesses, polarization impurities, BBR shifts, and imaging-heating conflation as first-class failure modes.

---

### Computational Physicist
**Agent file:** `agents/computational-physicist.md`

Reasons from governing equations, discretization, and HPC scaling through code/solution verification, DFT, MD, Monte Carlo, and FEM/FVM workflows (VASP, LAMMPS, COMSOL, OpenFOAM, QE).

---

### Condensed Matter Physicist
**Agent file:** `agents/condensed-matter-physicist.md`

Reasons from Bloch bands, quasiparticles, and symmetry through ARPES/STM/neutron/transport workflows, VASP/QE/Wannier90/DMFT, and Materials Project/ICSD/MPDS while treating matrix-element artifacts, Mott vs. DFT gaps, pseudogap vs. SC gap, and Planckian bad-metal transport as first-class failure modes.

---

### Experimental Physicist
**Agent file:** `agents/experimental-physicist.md`

Reasons from GUM error budgets, traceable calibration chains, and multiplied signal-chain transfer functions — separating Type A and Type B uncertainty, null runs, and ELN-linked reproducibility before precision or discovery claims.

---

### Fluid Dynamicist
**Agent file:** `agents/fluid-dynamicist.md`

Reasons from Navier–Stokes and dimensionless scaling through RANS/LES/DNS selection, mesh/y+ strategy, OpenFOAM/Fluent workflows, and MMS + ASME V&V 20 / PIV validation.

---

### Fusion Scientist
**Agent file:** `agents/fusion-scientist.md`

Reasons from Lawson triple product and Q through tokamak/stellarator confinement (H-mode, ELMs, RMP), NBI/ICRH/ECRH heating, EFIT/TRANSP/SOLPS-ITER workflows, ITER/JET/DIII-D/W7-X benchmarks, PMI (W/Be PFCs), and tritium breeding blankets.

---

### Gravitational Physicist
**Agent file:** `agents/gravitational-physicist.md`

Reasons from calibrated strain, colored non-stationary noise PSDs, matched-filter SNR, and Bayesian posteriors through PyCBC/GstLAL/cWB searches, Bilby/LALInference PE with NRSur/SEOBNR/IMRPhenom waveforms, and FAR/p_astro significance while treating glitch contamination, waveform-approximant mismatch, mass-spin and distance-inclination degeneracies, and unmodeled selection effects as first-class failure modes.

---

### Laser Physicist
**Agent file:** `agents/laser-physicist.md`

Reasons from population inversion and threshold gain (g ≥ l/L + T), ABCD resonator stability (g₁g₂ in 0–1) and c/(2L) mode spacing, GVD/TOD dispersion management and time-bandwidth ΔtΔν ≈ 0.44, and Kerr/SPM nonlinear phase through Kerr-lens/SESAM mode-locking, CPA stretcher–amplifier–compressor with B-integral budgeting, QPM in PPLN/PPLKTP for SHG/OPA, FROG/SPIDER and Dazzler pulse shaping, M² caustics per ISO 11146, and IEC 60825 classification while treating thermal-lens drift out of the stability zone, autocorrelation-width-mistaken-for-pulse-width, uncompensated TOD wings and regen double-pulsing, and LMA-fiber mode instability and SRS/SBS above kW as first-class failure modes.

---

### Low Temperature Physicist
**Agent file:** `agents/low-temperature-physicist.md`

Reasons from kT budgets, He-3/He-4 dilution refrigeration, and BCS/GL superconductivity; measures Tc, QHE, and Landauer conductance with lock-in/SQUID workflows while treating wiring heat loads, Kapitza resistance, flux trapping, TLS dielectric loss, and sample-vs-MXC thermometer mismatch as first-class failure modes.

---

### Metrology Scientist
**Agent file:** `agents/metrology-scientist.md`

Reason from SI traceability, GUM uncertainty budgets, and VIM distinctions between calibration and verification; propagates Type A/B components, CIPM MRA equivalence, and ILAC decision rules before any pass/fail claim.

---

### Nanophysicist
**Agent file:** `agents/nanophysicist.md`

Reasons from quantum confinement dimensionality, Coulomb diamonds and SET conditions, Kondo vs Luttinger-liquid power laws, and lock-in cryostat transport through STM/STS, AFM/KPFM, and STEM/EELS while treating charging artifacts, tip convolution, contact resistance, and beam-damage plasmon shifts as first-class failure modes.

---

### Nuclear Physicist
**Agent file:** `agents/nuclear-physicist.md`

Reasons from shell and collective structure, reaction mechanisms, and ENDF/EXFOR data; matches FRIB–CEBAF–RHIC science to R-matrix, Hauser-Feshbach, chiral ab initio, and GEANT4 tools; treats dead time, normalization, and evaluation covariances as first-class failure modes.

---

### Optical Physicist
**Agent file:** `agents/optical-physicist.md`

Reasons from quantized atom-field coupling, recoil and trap energy scales (Γ, E_rec, U/J, κ), and coupled instability-versus-systematic budgets through optical Bloch equations, in-situ lattice-depth and Rabi calibration, QuTiP and ARC modeling, and Allan-deviation and clock systematic tables, while treating uncalibrated lattice depth, intensity-noise heating, double-occupancy mimicking unity filling, and missing BBR or AC-Stark shifts as first-class failure modes.

---

### Particle Physicist
**Agent file:** `agents/particle-physicist.md`

Reasons from SM gauge structure, parton PDFs, and detector response through ATLAS/CMS/LHCb/Belle II/DUNE workflows, Geant4+Pythia/MG5 simulation, HistFactory/Combine/pyhf likelihoods, and HEPData/Rivet preservation while treating LEE/global significance, JES/pile-up, fake leptons, and flux×cross-section systematics as first-class failure modes.

---

### Photonics Scientist
**Agent file:** `agents/photonics-scientist.md`

Reasons from guided-wave dispersion, ring FSR–Q–coupling, and FWM phase matching; designs waveguides, lasers, and modulators with Lumerical MODE/FDTD/CHARGE/INTERCONNECT while treating dispersive FSR mismatch, TPA/FCA/XPM detuning, mesh dispersion, etalon ripples, and thermal bistability as first-class failure modes.

---

### Plasma Physicist
**Agent file:** `agents/plasma-physicist.md`

Reasons from collective scales (Debye length, plasma frequency), dimensionless regime parameters (beta, collisionality, Lundquist number), and instability drive-versus-dissipation through Grad-Shafranov equilibria (EFIT, VMEC), gyrokinetic and MHD codes (GENE, NIMROD, XGC), PIC simulation (VPIC, OSIRIS), and confinement scalings (IPB98, Greenwald, Troyon) while treating probe sheath distortion, equilibrium-reconstruction error, resolution-limited reconnection rates, and unmatched wall conditioning as first-class failure modes.

---

### Quantum Computing Scientist
**Agent file:** `agents/quantum-computing-scientist.md`

Reasons from qubits as noisy open systems through T1/T2, gate fidelity, RB/GST/XEB, and quantum volume to surface-code QEC; compiles with Qiskit/Cirq, applies ZNE/PEC/readout mitigation, and treats crosstalk, transpilation depth, and calibration drift as first-class failure modes.

---

### Quantum Information Scientist
**Agent file:** `agents/quantum-information-scientist.md`

Reasons from qubits as open systems, gate fidelities, and error correction while treating crosstalk and calibration drift as first-class failure modes.

---

### Quantum Optics Scientist
**Agent file:** `agents/quantum-optics-scientist.md`

Reasons from field quadratures, atom-photon coupling (g, κ, γ), and heralding efficiency budgets through g⁽²⁾ Hanbury Brown-Twiss measurement, balanced homodyne tomography, HOM interference, and SNSPD/APD detector calibration while treating afterpulsing-faked antibunching, LO phase drift erasing squeezing, accidentals and dark counts, and unaddressed Bell-test loopholes as first-class failure modes.

---

### Quantum Physicist
**Agent file:** `agents/quantum-physicist.md`

Reasons from Hilbert-space density operators, commutation relations, and Lindblad open-system dynamics through randomized benchmarking, gate-set and process tomography, Bell-CHSH tests, and Stim/PyMatching surface-code decoding while treating crosstalk, leakage, calibration drift, and measurement backaction as first-class failure modes.

---

### Semiconductor Physicist
**Agent file:** `agents/semiconductor-physicist.md`

Reasons from ε_n(k), effective-mass tensor, and 2D subband DOS through Hall/multiband fits, mobility scattering analysis, Lang DLTS (E_T, σ, N_T), and quantum-well intersubband spectroscopy while treating compensation, rate-window artifacts, and DFT gap error as first-class failure modes.

---

### Soft Matter Physicist
**Agent file:** `agents/soft-matter-physicist.md`

Reason from kT and mesoscale structure; couple rheology (TA Instruments, Anton Paar), scattering (SANS/SAXS/DLS/XPCS), and PIV to Flory-Huggins, de Gennes scaling, jamming, and active-matter hydrodynamics.

---

### Spintronics Physicist
**Agent file:** `agents/spintronics-physicist.md`

Reasons from spin-orbit coupling, spin diffusion length, exchange and DMI, and spin-dependent transport through MTJ/TMR characterization, ST-FMR and harmonic-Hall torque measurement, nonlocal spin valves, and Valet-Fert and MuMax3/OOMMF modeling, while treating barrier pinholes and shunt paths, ordinary-versus-anomalous Hall and ISHE confusion, Oersted-field and Joule-heating artifacts, and incomplete magnetization switching as first-class failure modes.

---

### Statistical Physicist
**Agent file:** `agents/statistical-physicist.md`

Reasons from ensembles and partition functions through finite-size scaling (Binder cumulant, data collapse), Wolff/cluster MC, and RG/MCRG to Jarzynski–Crooks fluctuation theorems; uses ALPS, NetKet, WHAM, and ED/DMRG while treating critical slowing down, subleading FSS humps, and poor work-histogram overlap as first-class failure modes.

---

### String Theorist
**Agent file:** `agents/string-theorist.md`

Reasons from worldsheet CFT anomaly cancellation, moduli stabilization, and effective-field-theory consistency through KKLT/LVS flux compactifications, KLT/CHY/BCFW amplitude methods, and AdS/CFT large-N holography while treating tadpole mismatches, runaway moduli, unstabilized de Sitter uplifts, and conjecture-as-theorem swampland overclaims as first-class failure modes.

---

### Surface Physicist
**Agent file:** `agents/surface-physicist.md`

Reasons from surface thermodynamics, adsorption coverage, work function, and probe escape depth through XPS/ARPES, LEED I(V) and CTR analysis, STM/AFM, TPD with Redhead analysis, and DFT slabs while treating adventitious-carbon contamination, differential charging, electron-beam and tip-induced damage, and UHV-to-operando extrapolation as first-class failure modes.

---

### Theoretical Physicist
**Agent file:** `agents/theoretical-physicist.md`

Reasons from symmetries, conservation laws, effective field theory, and limiting cases through Feynman-diagram and on-shell amplitude tools, renormalization-group flow, lattice and tensor-network numerics, and the conformal bootstrap, while treating gauge-dependent artifacts, unitarity and Ward-identity violations, scheme dependence, and lattice discretization errors as first-class failure modes.

---

### X Ray Synchrotron Scientist
**Agent file:** `agents/x-ray-synchrotron-scientist.md`

Reasons from photon-matter cross sections, reciprocal-space Q, absorption edges, and absorbed dose through pyFAI, GSAS-II, Athena/Artemis, BornAgain, and foil/silver-behenate calibration while treating fluorescence self-absorption, substrate Bragg misindexing, beam damage and radiation-induced reduction, and Fourier-termination ripples as first-class failure modes.

---

