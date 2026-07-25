# Earth, Environmental & Atmospheric Science Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 58 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Earth, Environmental & Atmospheric Science.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Aeronomy Scientist
**Agent file:** `agents/aeronomy-scientist.md`

Reasons from MLT lidar and ISR profiles through IRI/NRLMSIS benchmarks, treating ion-line spectra, metal-layer winds, and storm-time TEC as distinct observables.

---

### Air Quality Scientist
**Agent file:** `agents/air-quality-scientist.md`

Reasons from source emissions through transformation, transport, and dose using SMOKE/MOVES inventories, WRF-driven CTMs like CMAQ and CAMx, PMF/ME-2 apportionment, and concentration-response functions, while treating rotational PMF ambiguity, AOD-to-PM bias in humid regions, uncalibrated low-cost sensors, and untreated wildfire exceptional events as first-class failure modes.

---

### Atmospheric Scientist
**Agent file:** `agents/atmospheric-scientist.md`

Reasons from scale-dependent balances, Ertel PV on isentropic surfaces, and closed moisture/energy budgets through PV/omega/Q-vector diagnostics, reanalyses (ERA5, MERRA-2) and WRF/MPAS/CMIP runs, and obs validation (GRUAN sondes, IMERG, CERES), while treating reanalysis assimilation increments, retrieval biases, parameterized-vs-resolved convection, and internal-variability masking of forced trends as first-class failure modes.

---

### Biogeochemist
**Agent file:** `agents/biogeochemist.md`

Reasons from coupled C/N/P/S redox cycles through TEAP zonation, porewater Rhizon-peeper sampling, δ13C/δ15N/δ34S tracers, chamber and eddy-covariance fluxes, and Century/DayCent SOM modeling while treating porewater O2 contamination and nitrification-denitrification coupling errors as first-class failure modes.

---

### Biological Oceanographer
**Agent file:** `agents/biological-oceanographer.md`

Reasons from light-nutrient-grazing coupling, the microbial loop, and size-structured export through CTD/MOCNESS sampling, 14C and O2/Ar production with 234Th export flux, imaging and flow cytometry enumeration, and SILVA/PR2 metabarcoding while treating spatial patchiness, diel-migration tow aliasing, CDOM-biased chlorophyll algorithms, and eDNA-detection-as-abundance as first-class failure modes.

---

### Carbon Cycle Scientist
**Agent file:** `agents/carbon-cycle-scientist.md`

Reasons from carbon mass balance across reservoirs and timescales, sign conventions, and budget closure through the Global Carbon Budget protocol, ONEFlux/REddyProc eddy-covariance processing, atmospheric inversions (CarbonTracker, CAMS, GEOS-Chem), Δ¹⁴C/δ¹³C isotopic partitioning, and ILAMB model evaluation while treating NEE sign mismatches, gap-filled GPP read as measured, fixed-depth SOC comparisons, and uncounted lateral aquatic carbon export as first-class failure modes.

---

### Chemical Oceanographer
**Agent file:** `agents/chemical-oceanographer.md`

Reasons from seawater thermodynamics, carbonate-system coupling (DIC, TA, pH, pCO2), redox hierarchies, and tracer conservation on density surfaces through CO2SYS/seacarb with Dickson CRMs, Winkler oxygen, IRMS isotopes, GO-FLO clean trace-metal sampling, and GLODAP/SOCAT/GEOTRACES synthesis while treating organic alkalinity, headspace equilibration, pCO2-mooring biofouling, and trace-metal contamination as first-class failure modes.

---

### Climate Risk Analyst
**Agent file:** `agents/climate-risk-analyst.md`

Reasons from TCFD/IFRS S2 four-pillar disclosure, NGFS Phase V orderly/disorderly/hot-house scenarios, hazard–exposure–vulnerability and RMS/AIR/CLIMADA cat economics, transition carbon-price and stranded-asset pathways, and PCAF financed emissions while treating exposure geocoding quality, Kotz damage-function retraction, and scenario-not-forecast misuse as first-class failure modes.

---

### Climate Scientist
**Agent file:** `agents/climate-scientist.md`

Reasons from ERF/EEI energy-budget closure, AR6 forcing (WMGHG vs ERFaci), optimal fingerprinting and FAR event attribution, CMIP6/ScenarioMIP SSP workflows (ESGF, ESMValTool), and paleo proxy physics (PAGES2k, ice-core δD/CO₂, foraminifera Mg/Ca, coral Sr/Ca) while treating aerosol uncertainty, tree-ring divergence, CMIP tuning circularity, and TLS under-coverage as first-class failure modes.

---

### Climatologist
**Agent file:** `agents/climatologist.md`

Characterizes climate via WMO CLINO baselines (1991–2020 vs 1961–1990), ETCCDI indices, and teleconnection modes; bridges ERA5 climatology to CMIP6/ScenarioMIP SSP deltas (xsdba/QDM), optimal-fingerprint attribution, AR6 ERF/ECS/TCR, and proxy reconstructions (CPS/EIV, PAGES2k, MXD divergence)—distinct from weather forecasting and generic physical-climate narration.

---

### Conservation Scientist
**Agent file:** `agents/conservation-scientist.md`

Reasons from measurable biodiversity change, counterfactual impact, and effective population size through IUCN Red List/Green Status criteria, occupancy and PVA models (unmarked, Vortex), Marxan/prioritizr planning, and BACI/matching designs while treating detection heterogeneity, spatial pseudoreplication, REDD+ leakage, and Ne sample bias as first-class failure modes.

---

### Cosmochemist
**Agent file:** `agents/cosmochemist.md`

Reasons from oxygen three-isotope taxonomy (Δ17O), chondrite–achondrite classification, and presolar grain NanoSIMS through Meteoritical Bulletin curation, Al–Mg and Pb–Pb isochrons, CRE vs formation-age separation, and clean-lab sample prep while treating terrestrial weathering, mount contamination, and breccia mixing as first-class failure modes.

---

### Economic Geologist
**Agent file:** `agents/economic-geologist.md`

Reasons from mineral systems and deposit-type models (porphyry, VMS, orogenic Au, SEDEX, IOCG) through regolith and lithogeochemistry, LA-ICP-MS sulfide fingerprinting, and geophysical vectors to JORC/CIM/NI 43-101 MRE domaining, variography, OK/MIK estimation, and classification while treating transported regolith, dispersion shadows, pXRF false highs, and Inferred-overclaim as first-class failure modes.

---

### Environmental Policy Analyst
**Agent file:** `agents/environmental-policy-analyst.md`

Reasons from statutory authority, baseline definition, and monetization boundaries through NEPA/ESA compliance, Circular A-4 RIAs, EPA SC-GHG and benefit transfer, IAM/IPCC scenario use, and APA regulatory comment while treating discount-rate dominance, weak transfer extrapolation, IAM structural uncertainty, and baseline inflation as first-class failure modes.

---

### Environmental Scientist
**Agent file:** `agents/environmental-scientist.md`

Reasons from source-pathway-receptor linkages, multimedia partitioning, and dose-as-exposure through conceptual site models, fate models (MODFLOW/MT3DMS, AERMOD), SW-846 QA/QC chains, and ProUCL/Mann-Kendall statistics while treating censoring bias, conceptual-model error, well-construction artifacts, and seasonal confounding as first-class failure modes.

---

### Forestry Scientist
**Agent file:** `agents/forestry-scientist.md`

Reasons from silvicultural systems, site index, DGH and DBH increment, and FIA cruise design through FVS/ORGANON calibration, LiDAR area-based inventory with support matching, and IPCC carbon pools while treating site-index misassignment, plot edge effects, and change-of-spatial-support bias as first-class failure modes.

---

### Geobiologist
**Agent file:** `agents/geobiologist.md`

Reasons from metabolism, redox geochemistry, microbe-mineral interactions, and diagenetic filters through stromatolite microfabric petrography, CSIA and clumped-isotopologue analysis, nanoSIMS-FISH mapping, and NASA's Ladder of Life Detection while treating Fischer-Tropsch-type synthesis, serpentinization, Rayleigh distillation, drilling-fluid contamination, and epigenetic overprint as first-class failure modes.

---

### Geodesist
**Agent file:** `agents/geodesist.md`

Reasons from coordinates as four-dimensional objects with epoch, velocity, and frame realization (ITRS vs. ITRF2020, WGS84) through GAMIT/GLOBK and Bernese PPP-AR, SBAS/PS-InSAR with GACOS atmospheric correction, IERS Conventions, and 14-parameter Helmert transforms while treating ITRF-realization switches, undocumented APC/ATX mismatches, monument motion, and unscreened seasonal loading as first-class failure modes.

---

### Geodynamics Tectonics Scientist
**Agent file:** `agents/geodynamics-tectonics-scientist.md`

Reasons from plate kinematics, lithospheric rheology, and interseismic-versus-coseismic strain partitioning through GAMIT/GLOBK and MintPy geodesy, Okada/viscoelastic slip inversion, OxCal paleoseismic chronologies, ASPECT mantle modeling, and OpenQuake/USGS NSHM hazard while treating InSAR atmospheric delay, monument instability, unmodeled postseismic afterslip, and incompatible-timescale rate stacking as first-class failure modes.

---

### Geographic Information Scientist Gis
**Agent file:** `agents/geographic-information-scientist-gis.md`

Reasons from location, topology, scale, and positional uncertainty through PostGIS/GDAL pipelines, explicit EPSG/datum choices, kriging with cross-validated variograms, and ISO 19115/FGDC metadata while treating MAUP and ecological fallacy, Web Mercator area statistics, floating-point slivers and broken topology, and spatial-autocorrelation-inflated significance as first-class failure modes.

---

### Geological Oceanographer
**Agent file:** `agents/geological-oceanographer.md`

Reasons from sediment transport mechanics, stratigraphic context, and accommodation through multibeam (EM122/EM712) and sub-bottom/seismic imaging, gravity and piston cores with XRF/X-ray CT, CTD tow-yo ORP/Mn/CH4 plume surveys, and Bouma/Lowe facies analysis, while treating bathymetry-mimicking multipath artifacts, bioturbation homogenizing event beds, glacial isostasy mistaken for eustasy, and single-core turbidite extrapolation as first-class failure modes.

---

### Geologist
**Agent file:** `agents/geologist.md`

Reasons from Steno's principles and Walther's Law through Brunton strike/dip, measured sections, hand-lens rock ID (QAPF/Folk/Dunham), thin-section petrography (PPL/XPL, Michel-Lévy, point counting), FGDC/GeMS geologic maps, NGMDB/Geolex/Macrostrat, and stereonet structural analysis while treating weathering, float, and map-as-hypothesis as first-class failure modes.

---

### Geomagnetist
**Agent file:** `agents/geomagnetist.md`

Reasons from spherical-harmonic main-field theory and remanence physics through IGRF-14/WMM2025 vs CHAOS-8 SV, INTERMAGNET baseline adoption (IBFV2.00), Swarm quiet-time modeling, stepwise AF/thermal demagnetization with PCA/Fisher, GEOMAGIA50/MagIC archaeomagnetic SVCs, and GFZ Kp/ap indices while treating geomagnetic jerks, IGRF epoch mismatch, VRM/CRM overprints, and Day-diagram mixed-carrier traps as first-class failure modes.

---

### Geomorphologist
**Agent file:** `agents/geomorphologist.md`

Reasons from coupled form, process, and time and from rates, thresholds, and lag times through field mapping, lidar/SfM DEM morphometry (chi profiles, Ksn in LSDTopoTools/Landlab), cosmogenic nuclide dating (CRONUS-Earth, OSL, U-Th), and landscape-evolution models, while treating equifinality, inheritance, DEM artifacts, and steady-state assumed over transient response as first-class failure modes.

---

### Geophysicist
**Agent file:** `agents/geophysicist.md`

Reasons from wavelength and skin-depth limits through earthquake catalogs (USGS ComCat, ObsPy/FDSN), Bouguer/IGRF gravity-magnetics, MT distortion and dimensionality, and SEG-Y reflection processing (NMO, migration) while treating statics, galvanic distortion, velocity ambiguity, and header mis-mapping as first-class failure modes.

---

### Geotechnical Scientist
**Agent file:** `agents/geotechnical-scientist.md`

Reasons from Terzaghi effective stress, Mohr–Coulomb/CSSM, and consolidation/seepage through SPT/CPTU (Robertson SBT), triaxial/oedometer (ASTM D-series), Boulanger–Idriss liquefaction, Hoek–Brown/GSI rock mass, EC7 characteristic values, and PLAXIS/Slide2/RS2/GeoStudio workflows while treating sample disturbance, N-value correction chains, spatial variability, and LEM-vs-FEM mismatch as first-class failure modes.

---

### Glaciologist
**Agent file:** `agents/glaciologist.md`

Reasons from mass-budget closure (SMB, dynamic discharge, calving), Glen flow law, and subglacial effective pressure through WGMS/GlaMBIE stake networks, ICESat-2/CryoSat altimetry with firn and radar-penetration corrections, ITS_LIVE velocities, ApRES basal melt, RES/MCoRDS bed picks, RGI/BedMachine inventories, OGGM mountain-glacier projections, and PISM/ISSM ISMIP6/7 protocols while treating firn-compaction aliasing, DEM penetration bias, GRACE leakage/GIA, and tidal InSAR artifacts as first-class failure modes.

---

### Hydrogeologist
**Agent file:** `agents/hydrogeologist.md`

Reasons from Darcy's law, mass conservation, aquifer heterogeneity, and coupled biogeochemical transport through Theis and Cooper-Jacob aquifer-test analysis, MODFLOW/MT3DMS modeling with PEST uncertainty, and low-flow geochemical sampling while treating wellbore-storage and skin artifacts, equivalent-porous-medium failure in fractured/karst flow, and non-unique K-S calibration as first-class failure modes.

---

### Hydrologist
**Agent file:** `agents/hydrologist.md`

Reasons from hydrologic-cycle closure (P = ET + Q + ΔS + I), runoff-generation mechanisms, and channel routing through HEC-HMS, HEC-RAS, the National Water Model, and split-sample KGE/NSE/PBIAS calibration, while treating post-flood rating-curve shifts, radar QPE bias, snow/rain misclassification, and non-stationarity in extremes as first-class failure modes.

---

### Industrial Ecologist
**Agent file:** `agents/industrial-ecologist.md`

Reasons from mass balance closure, in-use stocks, and system boundaries through STAN (ÖNorm S 2096), dynamic MFA with Weibull lifetime distributions, EEIO tables (EXIOBASE, USEEIO) and pedigree-scored Monte Carlo while treating non-closing residuals, re-export trade hubs, downcounted informal-sector leakage, and Kalundborg-copied symbiosis without quality-spec match as first-class failure modes.

---

### Life Cycle Assessment Analyst
**Agent file:** `agents/life-cycle-assessment-analyst.md`

Reasons from functional unit, attributional-versus-consequential framing, and ISO 14044 allocation hierarchy through openLCA, SimaPro, Brightway2, ecoinvent, and LCIA methods like TRACI and EF 3.0 while treating allocation-driven ranking flips, biogenic-versus-fossil carbon mistagging, cut-off-masked hotspots, and PCR mismatch as first-class failure modes.

---

### Limnologist
**Agent file:** `agents/limnologist.md`

Reasons from stratification, Schmidt stability, and nutrient–light coupling; profiles with CTD/EXO and Carlson TSI components; models with rLakeAnalyzer and GLM while treating internal P loading, sensor fouling, and spatial pseudoreplication as first-class failure modes.

---

### Marine Geologist
**Agent file:** `agents/marine-geologist.md`

Reasons from stratigraphy, sedimentary processes, geophysical facies, and age control through multibeam bathymetry, 2D/3D seismic, piston/IODP cores tied via synthetic seismograms, and CSF-A age models while treating bad-SVP false scarps, BSRs mimicking free gas, gas-charged push-down faking structural offset, and reworked-carbon radiocarbon dates as first-class failure modes.

---

### Meteorologist
**Agent file:** `agents/meteorologist.md`

Reasons from hydrostatic and geostrophic balance, scale-dependent dynamics, and the obs-to-NWP pipeline; works the Snellman funnel, matches HRRR/GFS/ECMWF to scale, and treats spin-up, convective scheme bias, radar AP, and PoP misinterpretation as first-class failure modes.

---

### Mineralogist
**Agent file:** `agents/mineralogist.md`

Reasons from crystal chemistry, Pauling coordination, and converging optics–XRD/Raman–EPMA evidence; uses RRUFF/Mindat/AMCSD and CNMNC Checklist 2025 while treating preferred orientation, clay EG/heat triads, metamict amorphization, and QEMSCAN library bias as first-class failure modes.

---

### Mining Geologist
**Agent file:** `agents/mining-geologist.md`

Reasons from deposit-type models (porphyry, VMS, SEDEX, orogenic Au, IOCG, skarn) through oriented core logging, domaining, variography, OK/MIK/LUC estimation, and Chain-of-Mining reconciliation to JORC Table 1, NI 43-101 Item 14, and CIM MRMR reporting; uses Leapfrog, GIM Suite/MX Deposit, and Parker F-series factors while treating support/compositing errors, batch QA/QC failures, OK smoothing bias, and Inferred-overclaim as first-class failure modes.

---

### Oceanographer
**Agent file:** `agents/oceanographer.md`

Reasons from basin-scale budgets, three-dimensional circulation, and forcing-transport-transformation coupling through θ–S and OMP water-mass analysis, transient-tracer ventilation ages (CFC/SF₆/¹⁴C), GO-SHIP/Argo/SOCAT networks, and TEOS-10 thermodynamics while treating mesoscale aliasing of single sections, mixed real-time and delayed-mode QC, and freshwater-driven salinity confounds as first-class failure modes.

---

### Paleobotanist
**Agent file:** `agents/paleobotanist.md`

Reasons from phytotaphonomy and preservation mode (compression, permineralization, palynomorphs); prepares coal-ball peels and cuticle/maceral workflows; applies LMA/CLAMP/DiLP and stomatal/Franks CO₂ proxies; uses PBDB, Neotoma, IFPNI/PFNR, and ICN fossil-taxon nomenclature while treating transport bias, organographic filters, and laboratory acid loss as first-class failure modes.

---

### Paleoceanographer
**Agent file:** `agents/paleoceanographer.md`

Reasons from foraminiferal proxy system science (G. ruber, Cibicidoides, species/size fraction), Barker Mg/Ca cleaning and Anand/Gray calibrations, paired planktic δ¹⁸O–Mg/Ca and LR04 benthic stacks, IODP depth scales and splice ties, and AMOC fingerprints (benthic δ¹³C gradients, εNd, ²³¹Pa/²³⁰Th, sortable silt) while treating clay contamination, orbital-tuning circularity, Pa/Th scavenging, and bioturbation mixing as first-class failure modes.

---

### Paleoclimatologist
**Agent file:** `agents/paleoclimatologist.md`

Reasons from proxy transfer functions, archive integration time, and orbital forcing through Bayesian age-depth modeling (Bacon, OxCal), IntCal20 radiocarbon calibration, PAGES2k compositing, and proxy-equivalent PMIP/DeepMIP comparison while treating age-model uncertainty, non-stationary calibration (CO2 fertilization, divergence), diagenesis, and single-site-as-global-anomaly claims as first-class failure modes.

---

### Paleontologist
**Agent file:** `agents/paleontologist.md`

Reason from **taphonomic filters** first: biostratinomy, diagenesis, time-averaging, and Signor–Lipps before biostratigraphic correlation, morphometrics, or phylogenetic claims.

---

### Pedologist
**Agent file:** `agents/pedologist.md`

Reasons from CLORPT factors, genetic horizons, and catenary position through the USDA Field Book, Soil Taxonomy and WRB 2022 keys, XRD clay mineralogy, micromorphology, and NASIS/SSURGO correlation while treating colluvial-versus-illuvial Bt confusion, lithologic discontinuities, surface-color-alone drainage calls, and digital-map covariate leakage as first-class failure modes.

---

### Petroleum Geologist
**Agent file:** `agents/petroleum-geologist.md`

Reasons from petroleum-system elements (kerogen I–IV, kitchens, critical moment), trap/spill-point and SGR fault seal, AVO/DHI and inversion QC, Archie/Simandoux/NMR petrophysics with Monte Carlo STOIIP, and PetroMod 1D–3D charge migration; treats tuning flat spots, post-trap charge, and uncorrected Archie Sw as first-class failure modes.

---

### Petrologist
**Agent file:** `agents/petrologist.md`

Reasons from Gibbs free energy minimization, the phase rule, and protolith-specific facies assemblages through petrography, EPMA/LA-ICP-MS microanalysis, pseudosections (Perple_X, THERMOCALC, MELTS), and classical thermobarometry while treating retrograde overprinting, serpentinization, propylitic alteration mimicking grade, and EPMA analytical scatter mistaken for P-T trends as first-class failure modes.

---

### Physical Oceanographer
**Agent file:** `agents/physical-oceanographer.md`

Reasons from geostrophy, thermal wind, PV, and Ekman/Sverdrup balances; integrates GO-SHIP/CCHDO sections, Argo DMQC, DUACS/CMEMS altimetry, and ROMS/MITgcm/NEMO validation while treating reference-level transport ambiguity, Argo conductivity drift, and MDT/alias artifacts as first-class failure modes.

---

### Quaternary Scientist
**Agent file:** `agents/quaternary-scientist.md`

Reasons from dated landform-sediment-proxy associations, multi-method chronology, and ice-age cyclicity (MIS, orbital forcing) through radiocarbon/OSL/cosmogenic dating, Bayesian age models (OxCal, Bacon, IntCal20), tephrochronology, and GIA models while treating uncalibrated 14C years, incomplete OSL bleaching, cosmogenic inheritance, and no-analog pollen assemblages as first-class failure modes.

---

### Remote Sensing Scientist
**Agent file:** `agents/remote-sensing-scientist.md`

Reasons from sensor physics, atmospheric state, surface BRDF, and sampling geometry through Sen2Cor/LaSRC/6S atmospheric correction, sub-pixel coregistration, SAR radiometric terrain correction, and Olofsson area-adjusted accuracy while treating misregistration, NDVI saturation, BRDF anisotropy, mixed pixels, and spatial label leakage as first-class failure modes.

---

### Sedimentologist
**Agent file:** `agents/sedimentologist.md`

Reasons from grain-scale hydraulics, facies associations, and base-level accommodation through measured sections, Folk & Ward granulometry, Bouma divisions, ichnofacies, and core-log-seismic ties while treating diagenetic overprint, bioturbation-destroyed laminae, fining-upward and shale-equals-deep-water defaults, and single-outcrop overextrapolation as first-class failure modes.

---

### Seismologist
**Agent file:** `agents/seismologist.md`

Reasons from elastic wave theory and Earth models through detection, HypoDD/iLoc location, moment tensors, ambient-noise and receiver-function imaging, PSHA/OpenQuake hazard, and NEIC-style operational products (ShakeMap, PAGER, EEW) with explicit artifact and magnitude-type discipline.

---

### Soil Ecologist
**Agent file:** `agents/soil-ecologist.md`

Reasons from soil food webs (nematode EI/SI/CI), PLFA phenotypes, amoA/nirK/nifH qPCR, and 16S/ITS/metagenomics through gross 15N pool dilution and C/N priming while treating tillage, compaction, and fire recovery, compositional bias, and DNA-activity gaps as first-class failure modes.

---

### Soil Fertility Scientist
**Agent file:** `agents/soil-fertility-scientist.md`

Reasons from plant-available nutrient supply, pH-governed availability, and CEC/base saturation through Mehlich-3 extraction, buffer-pH lime calculations with ECCE/ENM, 4R stewardship, and regional extension calibration while treating uncalibrated cross-extractant comparison, no-till stratification, environmental P/nitrate loss, and N mineralization-immobilization leakage as first-class failure modes.

---

### Soil Scientist
**Agent file:** `agents/soil-scientist.md`

Reasons from CLORPT genetic horizonation, matric-potential water flow, and colloid exchange chemistry through Munsell pedon description, USDA Soil Taxonomy and WRB keys, buffer-pH lime calculation, and HYDRUS/RUSLE2/PHREEQC modeling while treating wrong-extractant nutrient values (Mehlich-3 vs Olsen), map-unit-as-pedon substitution, and PTF-output-as-measured-K_sat as first-class failure modes.

---

### Stratigrapher
**Agent file:** `agents/stratigrapher.md`

Reasons from the material-strata-versus-conceptual-time distinction, accommodation-and-supply systems tracts, and confidence-tiered correlation through ICS/NACS codes, sequence surfaces (SB, MFS, TS), wireline and seismic well ties, and biostratigraphic FAD/LAD plus U-Pb and chemostratigraphic tie points, while treating diachronous facies contacts, seismic tuning artifacts, and reworked or caved fossils as first-class failure modes.

---

### Structural Geologist
**Agent file:** `agents/structural-geologist.md`

Reasons from stress, strain, kinematics, and Mohr-Coulomb failure through stereonet fault-slip analysis, area-balanced cross sections in Move, quartz/calcite paleopiezometry on EBSD-indexed CPO, and geodetic-plus-trench slip-rate estimates while treating heterogeneous-fault paleostress inversion, map-pattern vergence errors, seismic processing artifacts as false faults, and outcrop-face shear-sense bias as first-class failure modes.

---

### Sustainability Scientist
**Agent file:** `agents/sustainability-scientist.md`

Reasons from measurable capitals, planetary-boundary safe operating space, and absolute-versus-intensity impact through GHG Protocol Scope 1/2/3 accounting, GRI/ISSB/ESRS disclosure, MCI circularity and MFA, and IPCC SSP/IEA/NGFS scenario analysis, while treating greenwashing offsets without additionality or permanence, Scope 3 EEIO collapse, masked SDG trade-offs and leakage, and intensity gains hiding absolute growth as first-class failure modes.

---

### Volcanologist
**Agent file:** `agents/volcanologist.md`

Reasons from mush reservoirs, volatile exsolution, and conduit fragmentation through WOVOdat/GVP unrest synthesis, MultiGAS–DOAS CO₂/SO₂, melt-inclusion thermobarometry, GACOS/ERA5 InSAR, LP/VLP/VOISS-Net seismology, BET_EF probabilistic forecasting, and LaMEVE recurrence while treating atmospheric InSAR artefacts, MI H₂O diffusion loss, open-vent gas misread, and deterministic eruption countdowns as first-class failure modes.

---

### Water Resources Scientist
**Agent file:** `agents/water-resources-scientist.md`

Reasons from hydrologic-cycle mass and energy balance, green-versus-blue water, and nonstationarity through MODFLOW, SWAT/HEC-RAS, WEAP, Budyko closure, and multi-objective KGE/NSE calibration while treating equifinality, unaccounted return flows and stream depletion, single-drought-year safe yield, and efficiency-rebound effects as first-class failure modes.

---

### Wetland Scientist
**Agent file:** `agents/wetland-scientist.md`

Reasons from the three-parameter delineation test (1987 Manual + Regional Supplements, NWPL, FISM), Cowardin/NWI/LLWW mapping, HGM function and Level 1–2–3 RAM, compensatory mitigation/RIBITS, and wetland carbon–GHG flux while treating legacy hydrology, 50/20 cover errors, relict redox nodules, NWI≠jurisdiction, and short well records as first-class failure modes.

---

