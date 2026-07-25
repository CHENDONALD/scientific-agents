# Agriculture, Food & Veterinary Science Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 27 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Agriculture, Food & Veterinary Science.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Agricultural Engineer
**Agent file:** `agents/agricultural-engineer.md`

Reasons from mass, energy, and momentum balances on variable biological media through ET-based scheduling, psychrometric grain-drying balances, ASABE D497 draft estimates, EPANET pipe networks, and RTK-GNSS/ISOBUS precision-ag validation while treating soil compaction, clogged drip emitters, grain-bin hotspots, GPS drift, and uncalibrated yield monitors as first-class failure modes.

---

### Agricultural Entomologist
**Agent file:** `agents/agricultural-entomologist.md`

Reasons from pest population dynamics, economic injury levels and thresholds, and degree-day phenology through systematic scouting, IRAC mode-of-action rotation, RCBD efficacy trials, and conservation biocontrol while treating misidentification, secondary pest flares from enemy removal, resistance under repeated MoA, and trap-catch-without-field-verification as first-class failure modes.

---

### Agroecologist
**Agent file:** `agents/agroecologist.md`

Reasons from socio-ecological farm systems, functional diversity, soil-biology-mediated fertility, and yield-service trade-offs through mother-baby and mixed-model trials, N/P/C mass balances, PLFA/amplicon and pollinator surveys, and NDVI/FRAGSTATS landscape analysis, while treating edge-effect and plot-size artifacts, weather-year confounding, surface-only soil carbon, and ignored labor/tenure adoption constraints as first-class failure modes.

---

### Agronomist
**Agent file:** `agents/agronomist.md`

Reasons from 4R stewardship and G×E×M through MRTN economic N, calibrated soil-test extractants, penetrometer compaction diagnosis, on-farm strip mixed models, partial budgets, and AgroEcoList reporting while treating pseudo-replication, yield-monitor drift, and yield-goal N over-application as first-class failure modes.

---

### Animal Nutritionist
**Agent file:** `agents/animal-nutritionist.md`

Reasons from NASEM/AAFCO requirements, SID amino acids and ideal protein, CNCPS MP/NE balance, and NANP feed libraries through NIR-wet chemistry validation, ileal vs fecal digestibility, pen-structured mixed models, and ARRIVE reporting while treating intake confounds, NIR calibration drift, acidosis/sorting, and pseudoreplicated pens as first-class failure modes.

---

### Animal Scientist
**Agent file:** `agents/animal-scientist.md`

Reasons from NRC nutrient requirements, ad libitum intake, energy/protein partitioning, and genotype x environment x management through ration software (CNCPS, NDS, NRC), pen-blocked trials with mixed models (lme4, PROC MIXED), and BCS, NIR, and rumen/BHBA diagnostics while treating intake collapse, milk fat depression, acidosis, heat stress, wrong experimental unit, and violated withdrawal times as first-class failure modes.

---

### Aquaculture Scientist
**Agent file:** `agents/aquaculture-scientist.md`

Reasons from FCR, dissolved oxygen and ammonia thresholds, hatchery biosecurity, and stock genetics while treating off-flavor, disease outbreak, and escape risk as first-class failure modes.

---

### Biosystems Agricultural Process Engineer
**Agent file:** `agents/biosystems-agricultural-process-engineer.md`

Reasons from coupled heat and mass transfer, moisture sorption (EMC/ERH on D245.7 isotherms), respiration, and closed unit-operation balances through ASABE standards (S352.2 oven moisture, S448 Page thin-layer kinetics, D272.3 airflow resistance), psychrometric aeration analysis, and SuperPro/Aspen bioprocess simulation while treating wet- vs dry-basis mixing, aeration that wets cool grain, case-hardened wet cores, and grain engulfment and dust explosion as first-class failure modes.

---

### Crop Protection Scientist
**Agent file:** `agents/crop-protection-scientist.md`

Reasons from IPM, EIL/ET, and FRAC/HRAC/IRAC MoA rotation through GEP/EPPO efficacy trials, CDMS label law, BBCH timing, DRT application, PPDB/fate modeling, and MRL/GAP alignment while treating resistance, drift, herbicide carryover, and abiotic mimicry as first-class failure modes.

---

### Crop Scientist
**Agent file:** `agents/crop-scientist.md`

Reasons from genotype-by-environment-by-management interaction, yield-component partitioning, and phenology-gated critical periods through MET stability analysis (AMMI, Finlay-Wilkinson, GGE biplots), mixed models (ASReml-R, lme4), N-response curves (quadratic-plateau, MRTN), and crop models (APSIM, DSSAT) while treating pseudo-replicated subsamples, single-site yield champions, uncorrected harvest moisture, and weather-during-anthesis confounding as first-class failure modes.

---

### Dairy Scientist
**Agent file:** `agents/dairy-scientist.md`

Reasons from the lactation curve, dry matter intake, and rumen health through NASEM Dairy 2021/CNCPS ration formulation, Penn State particle separation, DHIA records, and pen-level mixed models while treating subacute ruminal acidosis, milk fat depression, transition-cow hypocalcemia, and unadjusted DIM/parity confounding as first-class failure modes.

---

### Fermentation Scientist
**Agent file:** `agents/fermentation-scientist.md`

Reasons from Monod–Luedeking–Piret kinetics, overflow μcrit, OTR/RQ/RAMOS analytics, DoE media optimization, and 13C-MFA/COBRApy flux bounds while treating stuck-ferment ethanol×T synergy, SSF heat/moisture gradients, and OD-as-biomass red herrings as first-class failure modes.

---

### Fisheries Scientist
**Agent file:** `agents/fisheries-scientist.md`

Reasons from recruitment, growth, and natural and fishing mortality through state-space assessment models (SS3, SAM, JABBA), CPUE/GLM standardization, and reference points like F_MSY and B_lim under ICES and Magnuson-Stevens frameworks, while treating hyperstability, retrospective bias (Mohn's rho), unaccounted discard mortality, and misspecified M or selectivity as first-class failure modes.

---

### Food Chemist
**Agent file:** `agents/food-chemist.md`

Reasons from food matrix effects, aw and lipid oxidation, AOAC-validated HPLC/GC-MS/LC-MS/MS, FoodData Central/FNDDS, and trained sensory panels while treating matrix suppression, accelerated-shelf-life misuse, and untrained-taster data as first-class failure modes.

---

### Food Engineer
**Agent file:** `agents/food-engineer.md`

Reasons from water activity, thermal microbiology, transport-coupled reaction, and rheology through heat-penetration studies, F0/D/z lethality integration, HACCP with prerequisite programs, and CFR Title 21 LACF/acidified-food rules while treating cold-point under-processing, aw and pH drift, post-process contamination, and unvalidated scale-up as first-class failure modes.

---

### Food Microbiologist
**Agent file:** `agents/food-microbiologist.md`

Reasons from food as a hurdle-governed matrix of water activity, pH, and redox through BAM/ISO reference methods, c/n/m/M sampling plans, PMA-v-qPCR, and ComBase kinetics while treating VBNC and injured cells, post-process contamination, matrix inhibition, and unconfirmed PCR hits as first-class failure modes.

---

### Food Scientist
**Agent file:** `agents/food-scientist.md`

Reasons from a_w and GAB isotherms, Maillard/acrylamide kinetics, HLB emulsions, TPA/rheology, ISO sensory methods, and HACCP/FSMA preventive controls while treating aw–moisture conflation, HLB-only emulsion fixes, and Arrhenius misuse as first-class failure modes.

---

### Horticulturist
**Agent file:** `agents/horticulturist.md`

Reasons from plant-environment-cultural coupling, source-sink carbon partitioning, and chilling/photoperiod thresholds through rootstock-scion matching, DLI/VPD and substrate EC/pH targets, Dynamic/Utah chill models, and CA/MA postharvest setpoints while treating blossom-end rot, bitter pit, tipburn, storage scald, and MRL/PHI breaches as first-class failure modes.

---

### Plant Breeder
**Agent file:** `agents/plant-breeder.md`

Reasons from genetic variance, selection response (R = h²S), and breeding values through BLUP/GBLUP mixed models, multi-environment alpha-lattice trials with check cultivars, genomic selection validated within relatedness, and DUS/seed-certification standards, while treating linkage drag, G×E and G×management rank inversions, unvalidated GWAS hits, and seed mix-ups or off-type contamination as first-class failure modes.

---

### Plant Pathologist
**Agent file:** `agents/plant-pathologist.md`

Reasons from the disease triangle, sign vs. symptom, and trophic strategy (biotroph/necrotroph/hemibiotroph); runs clinic-to-Koch workflows (TWA isolation, Phytophthora pear baiting, Baermann nematodes, EPPO PM7/qPCR with matrix-specific Ct cutoffs) and epidemic analysis (AUDPC/AUDPS, Vanderplank parameters, GLMMs) while treating abiotic mimicry, saprophyte overgrowth, and late-cycle PCR artifacts as first-class failure modes.

---

### Poultry Scientist
**Agent file:** `agents/poultry-scientist.md`

Reasons from flock-level feed-to-gain conversion, digestible amino acid balance, and thermal/respiratory/pathogen load through FCR/EPEF and HDEP/HOF metrics, pen-or-house mixed models, coccidiosis lesion scoring, hatchery break-out, and strain management guides while treating subclinical coccidiosis and necrotic enteritis, wet-litter footpad dermatitis, pseudoreplicated subsampling, and woody-breast myopathy as first-class failure modes.

---

### Precision Agriculture Specialist
**Agent file:** `agents/precision-agriculture-specialist.md`

Reasons from management-zone heterogeneity, the spatial 4R (right input, rate, place, time), and per-zone margin maps through SSURGO/ECa zone delineation, NDVI/NDRE indices, RTK-GNSS georeferencing, and ISOBUS Task Controller as-applied logs while treating planned-versus-applied divergence, NDVI saturation, miscalibrated yield-monitor mass-flow and lag, and RTK float passes as first-class failure modes.

---

### Veterinarian
**Agent file:** `agents/veterinarian.md`

Reasons from species-specific physiology and pharmacology (Plumb's, AMDUCA, MDR1/PRiME), WSAVA 2024/AAHA/ISCAID 2025/CAPC guidelines, IDEXX/Cornell/eClinpath diagnostics, CMPS-SF/FGS pain and RECOVER 2024 CPR, and One Health zoonosis reporting while treating cat NSAID/acetaminophen toxicity, subclinical bacteriuria, greyhound lab artifacts, and human-dose extrapolation as first-class failure modes.

---

### Veterinary Epidemiologist
**Agent file:** `agents/veterinary-epidemiologist.md`

Reasons from herd-level units, Rogan–Gladen prevalence, R₀/SIR transmission models, and WOAH freedom-from-disease surveillance through outbreak line lists, SaTScan clusters, cluster field trials (REFLECT), and STROBE-Vet/AHSURED reporting while treating pseudo-replication, test-biased apparent prevalence, reporting-intensity clusters, and mis-specified generation intervals as first-class failure modes.

---

### Veterinary Microbiologist
**Agent file:** `agents/veterinary-microbiologist.md`

Reasons from pre-analytic specimen quality, CLSI VET01 AST, MALDI-TOF/PCR/WGS, and ISCAID significance thresholds through ACVM/AAVLD/WOAH workflows, NARMS/Vet-LIRN AMR surveillance, and One Health zoonoses while treating wound-swab contaminants, PCR-without-viability, human breakpoints on veterinary isolates, DTM false positives, MRSP biofilm, and Brucella BSL-3 exposure as first-class failure modes.

---

### Viticulturist Enologist
**Agent file:** `agents/viticulturist-enologist.md`

Reasons from source–sink canopy balance, terroir as water/nitrogen-mediated ripening, sugar–acid–phenolic trajectories, glucophilic AF and Oenococcus MLF, molecular SO₂ at pH, FOSS/OIV analytics, ISO 4120/QDA sensory, and NDVI selective harvest while treating stuck ferment (YAN/fructose), smoke glycoside release, pH-blind SO₂, and mineral-terroir folklore as first-class failure modes.

---

### Weed Scientist
**Agent file:** `agents/weed-scientist.md`

Reasons from the weed seed bank, population dynamics, and herbicide mode-of-action biology through log-logistic dose-response (GR50/GR90 in R drc), replicated RCB field trials with susceptible checks, molecular resistance assays (ALS sequencing, EPSPS copy number), and HRAC/WSSA-based MOA rotation while treating drift and carryover, tank-mix antagonism and water-quality failures, and late-escape seed rain as first-class failure modes.

---

