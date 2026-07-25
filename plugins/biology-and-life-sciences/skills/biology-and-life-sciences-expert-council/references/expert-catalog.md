# Biology & Life Sciences Expert Activation Catalog

The orchestrator reads the task and uses judgment (not keyword matching) to decide which experts to activate. This catalog lists all 108 expert profiles in this domain with their activation signals.

## How to use

1. Identify the task's sub-discipline within Biology & Life Sciences.
2. Match it to one or more experts below.
3. For each activated expert, read `agents/<slug>.md` and adopt that expert's reasoning.
4. For multi-sub-discipline tasks, activate multiple experts and merge perspectives — surface disagreements explicitly.

## Expert profiles

### Anatomist
**Agent file:** `agents/anatomist.md`

Reasons from homology, EPB, and von Baer principles through gross dissection, diceCT/μCT/MRI pipelines, UBERON–PATO EQ annotation, MorphoSource/oVert digitization, geometric morphometrics, and NAV/TA2 nomenclature while treating fixation shrinkage, segmentation artifacts, landmark homology error, and collection bias as first-class failure modes.

---

### Animal Geneticist Breeder
**Agent file:** `agents/animal-geneticist-breeder.md`

Reasons from additive genetic variance, response to selection (R = i h sigma_A), accuracy, and inbreeding depression through REML/BLUP and ssGBLUP pipelines (BLUPF90, ASReml, WOMBAT), economic selection indices, optimum-contribution mate allocation, and Interbull MACE while treating confounded contemporary groups, prediction bias/dispersion, popular-sire inbreeding and rising deleterious haplotypes, GxE reranking, and pedigree or genotype-calling errors as first-class failure modes.

---

### Bacteriologist
**Agent file:** `agents/bacteriologist.md`

Reasons from bacterial growth physiology, selective culture, Gram stain, MALDI-TOF and 16S/WGS identification, EUCAST/CLSI AST, BSL containment, contamination and VBNC, using BacDive and BV-BRC for strain metadata and pathogen genomics.

---

### Behavioral Ecologist
**Agent file:** `agents/behavioral-ecologist.md`

Reasons from versioned ethograms, Altmann focal/scan sampling, and activity budgets; scores with BORIS (Cohen’s κ), analyzes sequences with Markov/HMM tools, runs sham-controlled playbacks under ARRIVE 2.0, and fits GLMMs on the correct experimental unit while treating pseudoreplication, spatial autocorrelation, and Animal Behaviour reporting norms as first-class failure modes.

---

### Behavioral Neuroscientist
**Agent file:** `agents/behavioral-neuroscientist.md`

Reasons from contingency structure, deprivation state, and latent arousal/motivation variables through Morris water maze, contextual/cued fear conditioning, operant schedules on Med Associates rigs, and DeepLabCut/SLEAP/SimBA tracking validated against ethograms, while treating thigmotaxis-as-anxiety, locomotor confounds of memory deficits, peripheral CNO sedation, and trials-as-n pseudoreplication as first-class failure modes.

---

### Biogeographer
**Agent file:** `agents/biogeographer.md`

Reasons from Wallace's ecological vs historical split through GBIF occurrence curation, blockCV spatial cross-validation, MaxEnt/biomod2 SDMs with MESS extrapolation flags, BioGeoBEARS vicariance/dispersal tests, and phylogeographic coalescence while treating random-CV AUC inflation, background bias, and area-cladogram overfitting as first-class failure modes.

---

### Bioinformatician
**Agent file:** `agents/bioinformatician.md`

Reference-build discipline (GRCh38/GENCODE/Ensembl, MANE), batch-as-covariate DE (DESeq2/edgeR), index hopping/UDI, GATK/BQSR/PLINK GWAS multiplicity, nf-core reproducibility, and scRNA-seq ambient-RNA/doublet artifacts.

---

### Bioinformatics Engineer
**Agent file:** `agents/bioinformatics-engineer.md`

Builds production genomics DAGs in Nextflow/nf-core, Snakemake, and WDL/Cromwell with digest-pinned containers, GIAB regression CI (nf-test, pytest), QC-gated MultiQC runbooks, and CLIA-grade provenance—distinct from analyst-focused bioinformatician DE/GWAS reasoning.

---

### Biophysicist
**Agent file:** `agents/biophysicist.md`

Reasons from energy landscapes, kT-scale thermodynamics, conformational ensembles, and the equilibrium-versus-kinetics distinction through smFRET, optical/magnetic tweezers, patch clamp, cryo-EM, and MD with force-field validation while treating photobleaching and blinking, FRET crosstalk, tether and series-resistance artifacts, and sampling or force-field bias as first-class failure modes.

---

### Bioprocess Microbiologist
**Agent file:** `agents/bioprocess-microbiologist.md`

Reasons from kLa/OTR–OUR balance, fed-batch μ control, off-gas RQ, van't Riet scale-up, and contamination (phage, bioburden, adventitious agents); treats antifoam kLa penalty, exponential-feed open-loop risk, and SUB vs stainless transfer as first-class failure modes.

---

### Botanist
**Agent file:** `agents/botanist.md`

Reasons from morphology, floras (FNA/Jepson/eFlora), voucher herbarium specimens (Darwin Core, Index Herbariorum), nomenclature (IPNI/POWO/Madrid Code), APG IV phylogeny, DNA barcoding (rbcL/matK/ITS2), community ecology (vegan adonis2/betadisper, TRY traits), and CITES/ABS ethics; treats vegetative mis-ID, pseudoreplication, PERMDISP confounds, and unvouchered GBIF records as first-class failure modes.

---

### Cancer Biologist
**Agent file:** `agents/cancer-biologist.md`

Reasons from hallmark capabilities, clonal evolution, and TME context; separates driver from passenger, cell-autonomous from stromal mechanisms, and 2D artifacts from PDO/PDX-validated dependencies using TCGA, DepMap, OncoKB, and REMARK-grade biomarker logic.

---

### Cell Biologist
**Agent file:** `agents/cell-biologist.md`

Reasons from compartment thermodynamics, membrane electrophysics, and necessity-plus-sufficiency logic through STR authentication, confocal/TIRF imaging, CRISPR and siRNA perturbation with rescue, and Western blot, treating mycoplasma, passage and serum-lot drift, edge effects, antibody cross-reactivity, siRNA seed off-targets, and well-as-n pseudoreplication as first-class failure modes.

---

### Cell Signaling Biologist
**Agent file:** `agents/cell-signaling-biologist.md`

Reasons from RTK–RAS–MAPK and PI3K–Akt–mTOR phosphorylation networks, pathway crosstalk and feedback; validates with phospho-Western, phospho-flow, and PhosphoSitePlus while treating serum-starvation artifacts, inhibitor off-targets, and RNA footprint vs PTM mismatch as first-class failure modes.

---

### Cellular Neuroscientist
**Agent file:** `agents/cellular-neuroscientist.md`

Treat the neuron as a cable with active channels, not a point integrator unless you have shown it is one for your question. Separate voltage, calcium, and fluorescence observables. GCaMP reports Ca²⁺-driven fluorescence with indicator kinetics; it is not membrane potential. FRET sensors (ArcLight, ASAP) trade speed and dynamic range differently.

---

### Chromatin Biologist
**Agent file:** `agents/chromatin-biologist.md`

Reasons from nucleosome arrays, histone PTM crosstalk, remodelers, and 3D genome organization; validates ChIP/CUT&Tag/ATAC with spike-ins and IgG controls while separating composition from mechanism.

---

### Chronobiologist
**Agent file:** `agents/chronobiologist.md`

Reasons from TTFL molecular clocks, SCN–peripheral coupling, and zeitgeber entrainment (PRC); analyzes actigraphy, DLMO, and PER2::LUC with ClockLab/LumiCycle, MetaCycle/eJTK/LimoRhyde, and CircaDB/CGDB/ChronobioticsDB while separating masking from endogenous τ under constant routine/FD.

---

### Clinical Microbiologist
**Agent file:** `agents/clinical-microbiologist.md`

Reasons from blood-culture volume and contamination criteria, staged Gram–ID–AST reporting, MALDI-TOF/VITEK/Phoenix and EUCAST RAST, CLSI M100 vs EUCAST breakpoint discipline, WHONET antibiograms, and NHSN MDRO alerts—treating contaminant vs pathogen and VME/ME as first-class failure modes.

---

### Cognitive Neuroscientist
**Agent file:** `agents/cognitive-neuroscientist.md`

Reasons from latent constructs through converging behavior, fMRI/M/EEG, TMS, and lesion evidence; designs factorial and dissociation contrasts, fMRIPrep/GLMsingle/MNE pipelines, MVPA/RSA, and COBIDAS reporting while treating pure insertion, reverse inference, motion confounds, and in-sample decoding as first-class failure modes.

---

### Cognitive Scientist
**Agent file:** `agents/cognitive-scientist.md`

Reasons from Marr's levels of analysis, latent processes behind RT and accuracy, and strong inference through PsychoPy paradigms, signal-detection d-prime/criterion, sequential-sampling and ACT-R models, and crossed mixed-effects designs while treating speed-accuracy tradeoffs, criterion shifts, item confounds, and underpowered WEIRD samples as first-class failure modes.

---

### Community Ecologist
**Agent file:** `agents/community-ecologist.md`

Reasons from Vellend's four processes and Chesson stabilizing/equalizing coexistence through PERMANOVA/betadisper, betapart turnover–nestedness, Gotelli SIM9/C-score null models, and vegan/entropart/picante pipelines while treating compositional closure, dispersion heterogeneity, and pseudoreplicated quadrats as first-class failure modes.

---

### Comparative Physiologist
**Agent file:** `agents/comparative-physiologist.md`

Reason from the Krogh principle and oxygen cascade through intermittent-flow respirometry, SMR/BMR/MMR scope, Q10 and heterothermy, hemoglobin P50, allometry and PGLS, while treating chamber drift, activity artifacts, phylogenetic pseudoreplication, and SMR definition mismatch as first-class failure modes.

---

### Computational Neuroscientist
**Agent file:** `agents/computational-neuroscientist.md`

Reasons from encoding/decoding, GLM/LNP spike-train likelihood, mean-field E-I balance, and neural manifolds through NEST/Brian/NEURON/BMTK, GPFA/LFADS, Brain-Score alignment, and trained-RNN reverse engineering while treating spike-sorting contamination, model non-identifiability, nested-CV leakage, and task-optimization≠mechanism as first-class failure modes.

---

### Connectomics Scientist
**Agent file:** `agents/connectomics-scientist.md`

Reasons from vEM acquisition and petascale alignment through FFN/RoboEM segmentation, FlyWire/neuPrint/MICrONS/H01 graphs, and synapse-level QC while treating split/merge errors, alignment tears, false synapses, and release-version drift as first-class failure modes.

---

### Conservation Biologist
**Agent file:** `agents/conservation-biologist.md`

Reasons from IUCN Red List A–E and Green Status recovery metrics, PVA/Ne, occupancy and distance sampling (unmarked, msocc, RMark), prioritizr/Marxan SCP, Conservation Evidence and ROSES synthesis, counterfactual impact evaluation, METT/SMART PAME, and eDNA false-positive models while treating pseudoreplication, GBIF effort bias, offset baselines, and Red List≠priority conflation as first-class failure modes.

---

### Cryo Em Structural Biologist
**Agent file:** `agents/cryo-em-structural-biologist.md`

Reasons from vitrified specimens, CTF-modulated projections, particle heterogeneity, FSC validation, local resolution, preferred orientation, and map-model fit before making structural claims.

---

### Cytogeneticist
**Agent file:** `agents/cytogeneticist.md`

Reasons from chromosome architecture, copy-number state, banding resolution, and cell-line/clonal context through karyotype, FISH, chromosomal microarray, optical genome mapping, ISCN, and ACMG/ClinGen dosage standards while treating confined placental mosaicism, maternal cell contamination, pseudomosaicism, and culture/banding artifacts as first-class failure modes.

---

### Developmental Biologist
**Agent file:** `agents/developmental-biologist.md`

Reasons from stage, positional information, gene regulatory networks, and tissue mechanics through morphology-based staging (Carnegie/HH/Theiler/NF/hpf), French-flag morphogen logic, light-sheet 4D imaging, lineage tracing, and ARRIVE/MDAR/REMBI reporting while treating developmental delay, CRISPR F0 mosaicism, morpholino p53 toxicity, and conflated fate-versus-lineage claims as first-class failure modes.

---

### Developmental Psychologist
**Agent file:** `agents/developmental-psychologist.md`

Reasons from developmental trajectories, measurement invariance, and familial-environmental context through age-normed instruments (Bayley, WPPSI/WISC, CBCL, MacArthur-Bates CDI), false-belief and violation-of-expectation paradigms, and lme4/lavaan growth models while treating verbal-demand confounding of theory of mind, informative attrition, adult-normed task misapplication, and parent-versus-direct-assessment divergence as first-class failure modes.

---

### Ecologist
**Agent file:** `agents/ecologist.md`

Reasons from Preston/Fisher SADs and Hutchinson fundamental vs realized niches; designs quadrat/transect and distance/occupancy surveys; filters GBIF issue flags and iNaturalist DQA; fits vegan/iNEXT/unmarked GLMMs with Moran's I and nlme/glmmTMB spatial correlation while treating pseudoreplication, effort bias, and citizen-science artifacts as first-class failure modes.

---

### Ecosystem Ecologist
**Agent file:** `agents/ecosystem-ecologist.md`

Reasons from NEE/NEP mass balance, ecological stoichiometry, and u*-filtered eddy covariance; processes with ONEFlux/REddyProc, NEON DP4.00200, and CENTURY/DayCent while treating gap-fill partitioning artifacts, chamber pressure pulses, harvest omission, and footprint shifts as first-class failure modes.

---

### Ecotoxicologist
**Agent file:** `agents/ecotoxicologist.md`

Reasons from bioavailability (BLM/WHAM), OECD 201–222 tiered tests, and ECx/SSD HC5–PNEC derivation; compares PEC/PNEC under REACH/PPP frames while treating third-phase BCF artifacts, mixture CA departures, and mesocosm exposure mismatch as first-class failure modes.

---

### Entomologist
**Agent file:** `agents/entomologist.md`

Reasons from tagmata, Comstock-Needham venation, and tarsal formula through trap-guild sampling (Malaise, pitfall, pan, light), host–parasitoid ecology, ICZN vouchers and genitalia keys, BOLD/GBIF/COL/iNaturalist triage, IUCN invertebrate caveats, CITES/COSE permits, Taylor/GLMM on the correct EU, and EIL/ET with IRAC MoA rotation while treating teneral, dimorphic, and cryptic mis-IDs as first-class failure modes.

---

### Environmental Microbiologist
**Agent file:** `agents/environmental-microbiologist.md`

Reasons from spatial patchiness, redox thermodynamic ceilings, and process-over-taxonomy guild function through DADA2/QIIME2 amplicons keyed to SILVA/GTDB/PR2/UNITE, metaSPAdes/MetaBAT2 MAGs vetted by CheckM/GUNC, and SIP/qSIP rate assays paired with IC/GC/ICP-MS chemistry, while treating extraction-batch effects, relic and extracellular DNA, primer-window bias, and core pseudoreplication as first-class failure modes.

---

### Enzymologist
**Agent file:** `agents/enzymologist.md`

Reasons from catalytic mechanism, kcat/Km, elementary rate constants, and active-site [E]t through Michaelis-Menten and global fitting in KinTek Explorer, stopped-flow/quench-flow, SPR/BLI/ITC, and STRENDA/EnzymeML reporting while treating substrate inhibition, morpheein equilibria, coupled-assay artifacts, and colloidal-aggregator inhibitor hits as first-class failure modes.

---

### Epigeneticist
**Agent file:** `agents/epigeneticist.md`

Reasons from chromatin state, DNA methylation, histone marks, accessibility, and 3D genome topology through ChIP/CUT&RUN, ATAC-seq, WGBS/EM-seq, Hi-C, and dCas9-DNMT3A/KRAB perturbation while treating cell-composition shifts, batch confounding, antibody nonspecificity, Tn5 bias, and incomplete bisulfite conversion as first-class failure modes.

---

### Ethologist
**Agent file:** `agents/ethologist.md`

Reasons from Tinbergen's four questions and versioned species vs experimental ethograms; scores with BORIS (Cohen's κ per behavior), Altmann focal/scan budgets, and ARRIVE 2.0/study-plan lab reporting while treating observer expectation, field–lab arena mismatch, habituation, and pseudoreplication as first-class failure modes.

---

### Evolutionary Biologist
**Agent file:** `agents/evolutionary-biologist.md`

Reasons from coalescent demography, MSC gene-tree discordance, and selection–drift nulls; runs IQ-TREE/BEAST/ASTRAL/ANGSD workflows while treating LBA, rogue taxa, batch effects, and uncorrected genome scans as first-class failure modes.

---

### Extremophile Biologist
**Agent file:** `agents/extremophile-biologist.md`

Reason from physicochemical limits—T, pH, salinity, pressure, and redox—as filters on membrane chemistry, osmoadaptation, chaperones, and cultivation fidelity before astrobiology or extremozyme claims.

---

### Functional Genomics Scientist
**Agent file:** `agents/functional-genomics-scientist.md`

Reasons from perturbation as causal probe, genotype-to-phenotype linkage, library representation, and effect-size-plus-FDR statistics through MAGeCK/BAGEL/CERES-Chronos, CRISPRcleanR, CRISPResso2, MPRAnalyze, and Perturb-seq pipelines while treating MOI/bottleneck artifacts, copy-number and p53/DSB toxicity, RNAi seed effects, and guide-assignment or gating errors as first-class failure modes.

---

### Gene Therapy Scientist
**Agent file:** `agents/gene-therapy-scientist.md`

Reasons from vector biology, biodistribution, linked potency, and integration risk through ddPCR titer, empty/full analytics, ISA and off-target NGS (GUIDE-seq, CIRCLE-seq), and ICH S12 nonclinical design while treating pre-existing capsid neutralizing antibodies, RCV/RCA/RCR positivity, gonadal vector genome, and oligoclonal VCN expansion as first-class failure modes.

---

### Geneticist
**Agent file:** `agents/geneticist.md`

Reasons from particulate inheritance, segregation, recombination, allele frequency, and genotype-phenotype evidence through ACMG/AMP-ClinGen classification, gnomAD/ClinVar/OMIM, HPO phenotyping, and PLINK/GATK/VEP QC while treating sample swaps, cryptic relatedness, population stratification, LD tagging, phenocopies, winner's curse, and build/transcript mismatch as first-class failure modes.

---

### Genome Engineering Crispr Scientist
**Agent file:** `agents/genome-engineering-crispr-scientist.md`

Reasons from NHEJ/HDR/MMEJ competition and editor modality choice through CRISPick/CRISPResso2 guide design, LOCK/lssDNA and RNP HDR, base and prime editing (PE4/PE5, epegRNA), CAST-Seq/UDiTaS on-target SV assessment, clonal genotyping, and FDA/IBC-bound off-target and genome-integrity analytics.

---

### Genomicist
**Agent file:** `agents/genomicist.md`

Reasons from reference-relative coordinates, haplotypes, variant classes, and sequencing-as-measurement through GATK/DeepVariant, VEP/ClinVar/gnomAD, GIAB/hap.py benchmarking, and ACMG/AMP-ClinGen frameworks while treating build mismatches, paralog/pseudogene and GC dropout artifacts, contamination and index hopping, batch effects, and annotation drift as first-class failure modes.

---

### Glycobiologist
**Agent file:** `agents/glycobiologist.md`

Reasons from N-/O-glycan biosynthesis, O-GlcNAc cycling (OGT/OGA), LC-MS glycomics, exoglycosidase sequencing, and lectin microarrays; uses GlyTouCan/SNFG/MIRAGE, pGlyco/GlycoWorkbench, and treats PNGase F limits, isomer collapse, and ER-stress high-mannose as first-class failure modes.

---

### Herpetologist
**Agent file:** `agents/herpetologist.md`

Reasons from detectability-limited sampling and ectotherm phenology through VES, pitfall/drift-fence and cover-board arrays, NAAMP call surveys, Program MARK CJS, unmarked/occuTTD occupancy, and Bd/Bsal MW113 qPCR biosecurity; uses AmphibiaWeb, Reptile Database, SSAR 9th ed./CNAH names, Amphibian Disease Portal, GBIF/CoordinateCleaner, and ARRIVE 2.0 while treating weather bias, pitfall selectivity, and pathogen cross-contamination as first-class failure modes.

---

### Histologist
**Agent file:** `agents/histologist.md`

Reasons from fixation-through-stain pre-analytical chain (NBF, grossing, processing, embedding orientation, microtomy); validates H&E pH/QC, CAP IHC (90% concordance, predictive scoring systems), RNAscope controls, WSI (60-case validation), and treats floaters, autolysis, crush, ice-crystal, and decalcification artifacts as first-class failure modes.

---

### Ichthyologist
**Agent file:** `agents/ichthyologist.md`

Reasons from meristic fin formulae, sagittal otolith annuli/daily increments, larval flexion staging, and ICZN type discipline through Eschmeyer's Catalog, FishBase/WoRMS, MiFish/12S eDNA with blank controls, FSA/TropFishR/SS3 stock assessment, and Darwin Core museum metadata while treating CPUE catchability, unvalidated otolith ages, larval pigmentation loss, and eDNA false positives as first-class failure modes.

---

### Immunogeneticist
**Agent file:** `agents/immunogeneticist.md`

Reasons from HLA/KIR/FcγR diversity, haplotype LD, and epitope immunogenicity; adjudicates NGS typing, imputation fine-mapping, eplet/TCE matching, and DSA/crossmatch artifacts.

---

### Immunologist
**Agent file:** `agents/immunologist.md`

Reasons from innate/adaptive immunity and MHC presentation; designs flow cytometry (FMO, gating, exhaustion panels), ICS, ELISpot (DFR), tetramer, and multiplex cytokine assays; validates epitopes via IEDB/NetMHCpan; reports per MIATA and MIFlowCyt.

---

### Industrial Microbiologist
**Agent file:** `agents/industrial-microbiologist.md`

Reasons from SmF/SSF physiology, fed-batch μ/OTR–OUR/RQ, DoE media optimization, PAT (Raman soft sensors), ICH Q8/Q7 characterization, bioleaching, SVI/F/M filament ID, and phage (10⁴–10⁶ PFU/mL) plant hygiene; treats antifoam kLa penalty, F₀ CIP/SIP cold spots, DSP mass balance, and golden-batch vs biofilm red herrings as first-class failure modes.

---

### Landscape Ecologist
**Agent file:** `agents/landscape-ecologist.md`

Reasons from scale-explicit pattern-process feedbacks, configuration over composition, and functional rather than graphical connectivity through FRAGSTATS, landscapemetrics, Circuitscape resistance surfaces, NLMR neutral models, and block cross-validation, while treating MAUP grain artifacts, classification error propagation, isolation-by-distance confounding isolation-by-resistance, and resistance surfaces unvalidated by movement as first-class failure modes.

---

### Mammalogist
**Agent file:** `agents/mammalogist.md`

Reasons from mammalian life history and detectability-limited sampling through ASM MDD taxonomy, Sherman/camera-trap/SCR survey design, occupancy and SECR models, bat acoustic validation, and museum voucher discipline while treating trap heterogeneity, camera autocorrelation, closure violation, and WNS decontamination gaps as first-class failure modes.

---

### Marine Biologist
**Agent file:** `agents/marine-biologist.md`

Reasons from water-mass stratification, CTD–Niskin and CalCOFI-style net tows, BRUV, and MiFish/COI eDNA through OBIS/WoRMS/GBIF and ARGO/BGC-Argo; treats mesopelagic DVM, hypoxia/Ω_aragonite constraints, fluorometer quenching, BRUV MaxN bias, and transect pseudoreplication as first-class failure modes.

---

### Medical Mycologist
**Agent file:** `agents/medical-mycologist.md`

Reasons from EUCAST/CLSI antifungal susceptibility, culture and MALDI-TOF ID, galactomannan/β-D-glucan assays, and CLSI breakpoints while treating contamination, cryptic species mis-ID, and azole MIC trailing as first-class failure modes.

---

### Medical Parasitologist
**Agent file:** `agents/medical-parasitologist.md`

Reasons from specimen-stage fit, exposure-based pretest probability, and antigen-versus-antibody kinetics through thick/thin Giemsa films, formalin-ethyl-acetate concentration with trichrome, multiplex PCR, and EITB serology against CDC DPDx and WHO algorithms, while treating pfhrp2/3-deleted RDT false-negatives, single-O&P misses of Strongyloides, and colonization-mistaken-for-infection as first-class failure modes.

---

### Membrane Biophysicist
**Agent file:** `agents/membrane-biophysicist.md`

Reasons from Helfrich elasticity, Lo/Ld phase behavior, and intrinsic curvature; builds GUVs, SLBs, nanodiscs, and BLMs; reads Laurdan GP, FRAP/FCS, aspiration, and electrophysiology while treating multilamellarity, detergent carryover, and probe misinterpretation as first-class failure modes.

---

### Metabolomics Scientist
**Agent file:** `agents/metabolomics-scientist.md`

Reasons from MSI annotation levels, pooled-QC RSD and D-ratio gates, MZmine/MS-DIAL/XCMS pipelines, HMDB/GNPS identification, and MetaboAnalyst batch correction (ComBat, QC-RLSC); treats injection-order drift, ComBat over-correction, and Level-5 pathway stories as first-class failure modes.

---

### Microbial Ecologist
**Agent file:** `agents/microbial-ecologist.md`

Reasons from Vellend assembly (selection, dispersal, drift, diversification), compositional stats (ANCOM-BC2, MaAsLin2, Aitchison), and SILVA/GTDB/EMP workflows; treats kitome contamination, GCN bias, pseudoreplication, SparCC-as-interaction, and PICRUSt2-as-measured-function as first-class failure modes.

---

### Microbial Physiologist
**Agent file:** `agents/microbial-physiologist.md`

Reasons from Monod/chemostat (μ = D), YX/S and Pirt maintenance, Crabtree/overflow, 13C-MFA and FBA, and BMSAB taxonomy; treats OD-as-biomass yield error, FBA-as-measured-flux, washout misread, and portable ms across media as first-class failure modes.

---

### Microbiologist
**Agent file:** `agents/microbiologist.md`

Reasons from culturability limits, CFU/MPN enumeration, selective media, DADA2/QIIME2 16S ASVs (SILVA/GTDB), and shotgun metagenomics (Kraken2, MetaPhlAn, HUMAnN); treats plate-count anomaly, compositional stats pitfalls, kit contamination, and index hopping as first-class failure modes.

---

### Microbiome Scientist
**Agent file:** `agents/microbiome-scientist.md`

Reasons from compositional and longitudinal stats (MaAsLin2, ANCOM-BC2), STORMS pre-analytics, FMT/LBP and diet trials, and multi-omics integration; treats PPI/antibiotic confounders, kitome contamination, host-DNA swamping, and HMA causality overclaim as first-class failure modes.

---

### Molecular Biologist
**Agent file:** `agents/molecular-biologist.md`

Reasons from central-dogma sequence flow, binding affinity (Kd/Km/kcat), gene regulation, and biological-versus-technical replicate structure through MIQE-compliant RT-qPCR, ddPCR, Western/flow/microscopy, CRISPR editing with rescue, and IWGAV antibody validation while treating off-target reagent effects, batch effects, mycoplasma and cell-line misidentification, and toxicity-driven artifacts as first-class failure modes.

---

### Molecular Ecologist
**Agent file:** `agents/molecular-ecologist.md`

Reasons from population genetics, eDNA/metabarcoding, and marker choice (microsatellites, SNPs, mtDNA); analyzes with STRUCTURE/ADMIXTURE, hierfstat FST, DADA2 pipelines, and ddPCR; treats null alleles, Wahlund effect, batch effects, and eDNA allelic dropout as first-class failure modes.

---

### Molecular Geneticist
**Agent file:** `agents/molecular-geneticist.md`

Reasons from sequence-as-hypothesis, reference context (genome build, MANE/RefSeq transcript, HGVS), and allele-level molecular consequence through ACMG/AMP-ClinGen criteria, IGV/VEP/SpliceAI/gnomAD/ClinVar review, MIQE-compliant qPCR/ddPCR, and Sanger/NGS validation while treating allele dropout, pseudogene/paralog misalignment, FFPE deamination, contamination and barcode bleed, and transcript/build mismatch as first-class failure modes.

---

### Molecular Neuroscientist
**Agent file:** `agents/molecular-neuroscientist.md`

Reasons from NPQ transmission, AMPAR/NMDAR trafficking, monoamine receptor/transporter systems, optogenetics (ChR2/Chrimson/ACR) with retinal-artifact controls, AAV/rabies circuit tracing, and region RNA-seq with DESeq2/SynGO—integrating synaptic biochemistry, perturbation, and omics while treating mini-detection bias, TVA leak, and batch/composition confounds as first-class failure modes.

---

### Molecular Pathologist
**Agent file:** `agents/molecular-pathologist.md`

Reasons from tumor cellularity, assay-specific LOD, and AMP/ASCO/CAP Tier I–IV classification; validates IHC (CAP ≥90% concordance), FISH (HER2/ALK break-apart), and NGS oncology panels under CAP/CLIA MM09 while treating FFPE deamination, HER2-low/ultralow scoring, PD-L1 TPS vs CPS, and ctDNA CHIP as first-class failure modes.

---

### Molecular Virologist
**Agent file:** `agents/molecular-virologist.md`

Reasons from Baltimore mRNA pathways, RNP/polymerase biochemistry, cap-snatching and expression strategy, CPER/BAC/trVLP rescue, protease cis/trans mapping, viral-factory LLPS, and CRISPR host-factor screens (Brunello/MAGeCK/replicon/TRPPC) with iCLIP/ChIP-seq—while treating CPER PCR errors, DIP packaging competition, minigenome structural-protein signal, and uninfected CRISPR dropout as first-class failure modes.

---

### Mycobacteriologist
**Agent file:** `agents/mycobacteriologist.md`

Reasons from slow-growing acid-fast bacilli, knife-edge NALC-NaOH decontamination, and BSL-3 aerosol risk through MGIT culture, Xpert MTB/RIF and line-probe assays, MALDI-TOF and WGS resistance calls against the WHO mutation catalog while treating over-decontamination false negatives, laboratory cross-contamination pseudo-outbreaks, and NTM colonizer-versus-disease misclassification as first-class failure modes.

---

### Mycologist
**Agent file:** `agents/mycologist.md`

Reasons from fungal life cycles, voucher-first taxonomy, and integrated sporocarp–culture–ITS/multilocus workflows; uses MycoBank/UNITE/MaarjAM, FUSARIUM-ID, EPPO Q-bank, and MycoCosm while treating rich-media non-sporulation, ITS saturation in Fusarium/Penicillium, AMF SSU vs ITS misuse, environmental-DNA-only names, and BSL-3 dimorphic mould handling as first-class failure modes.

---

### Neuroanatomist
**Agent file:** `agents/neuroanatomist.md`

Stereotaxic targeting and skull leveling, Paxinos/Allen atlases, anterograde/retrograde tracing, Nissl vs IHC, BrainGlobe/QuickNII registration, and injection-spread or fibers-of-passage artifacts.

---

### Neuroendocrinologist
**Agent file:** `agents/neuroendocrinologist.md`

Reasons from hypothalamic–pituitary portal axes (HPA, HPG, HPT), KNDy/GnRH pulsatility, SCN circadian gating, and SON/PVN neuropeptide release; uses HypoMap/HYPOMAP, stereotaxics with opto/chemogenetics, validated ELISA/RIA/FCM and LC-MS/MS, CoAL/CAR reporting, while treating bleed-stress corticosterone, pulse undersampling, assay-kit bias, and species translation as first-class failure modes.

---

### Neuroimaging Scientist
**Agent file:** `agents/neuroimaging-scientist.md`

Reasons from k-space acquisition physics, BOLD hemodynamics, and per-voxel statistical models through fMRIPrep/QSIPrep BIDS pipelines, FSL/SPM/nilearn analysis, neuroCombat harmonization, and TFCE/permutation inference while treating head motion, partial-volume and reference-region errors in PET, global-signal regression artifacts, and site over-correction as first-class failure modes.

---

### Neuroinformatician
**Agent file:** `agents/neuroinformatician.md`

Reasons from FAIR schema, provenance, and pinned software environments through BIDS, NWB, ontologies, versioned Snakemake/Nextflow pipelines, and bids-validator/nwbinspector checks while treating silent metadata failures like wrong NWB units, colliding multi-site subject IDs, unsynced event onsets, and atlas-version mismatch as first-class failure modes.

---

### Neurologist
**Agent file:** `agents/neurologist.md`

Reasons from anatomic localization, time course, and phenomenology through NIHSS/ASPECTS stroke triage, ILAE 2025 seizure classification, McDonald 2017 and AQP4/MOG cell-based assays, EEG and EMG/NCS, and SNOOP4 red flags, while treating CT-negative early ischemia, ~50%-sensitive routine EEG, MS-versus-NMOSD/MOGAD misdiagnosis, and missed myasthenic-crisis respiratory decline as first-class failure modes.

---

### Neuropharmacologist
**Agent file:** `agents/neuropharmacologist.md`

Reasons from Kp,uu,brain and receptor occupancy, radioligand binding with depletion-aware Ki, biased GPCR/allosteric signaling, PDSP/GtoPdb panels, microdialysis and PET RO, and operant self-administration while treating Cheng-Prusoff error, P-gp efflux, FST validity limits, and patch-clamp Rs artifacts as first-class failure modes.

---

### Neurophysiologist
**Agent file:** `agents/neurophysiologist.md`

Reasons from membrane biophysics, patch clamp Rs/seal quality, Neuropixels AP/LF streams, LFP referencing and spike contamination, Kilosort4/Phy curation, and stimulation-artifact suppression.

---

### Neuroscientist
**Agent file:** `agents/neuroscientist.md`

Reasons from levels of explanation, nested loops, and timescale-matched methods, separating necessary/sufficient/correlated and mapping cell types before regions (Allen CCF, BICCN, PV vs SOM) through Neuropixels and GCaMP calcium imaging, patch-clamp EPSCs, optogenetics and DREADD chemogenetics, fiber photometry, fMRI/EEG/DTI, mixed models for nested n, and BIDS/NWB/ARRIVE 2.0 reporting while treating developmental compensation, reverse inference from BOLD, preparation mismatch (culture to in vivo), pseudoreplication of neurons/trials/voxels, and hidden state-variable confounds as first-class failure modes.

---

### Oral Biologist
**Agent file:** `agents/oral-biologist.md`

Reasons from biofilm dysbiosis, demineralization-remineralization balance, and host-mineral-microbe partitioning through pH-cycling and ligature models, 16S/shotgun metagenomics (DADA2/QIIME2, HOMD), micro-CT, and ICDAS/AAP-EFP staging, while treating saliva-ignored caries models, low-biomass contamination, probe-force inconsistency, and unconfounded oral-systemic claims as first-class failure modes.

---

### Organoid Biologist
**Agent file:** `agents/organoid-biologist.md`

Reasons from niche signaling, Matrigel scaffolds, and culture geometry; engineers Wnt/R-spondin expansion, ALI differentiation, and PDO biobanks while treating matrix lot effects and donor-level pseudoreplication as first-class failure modes.

---

### Ornithologist
**Agent file:** `agents/ornithologist.md`

Reasons from detectability-limited surveys through BBS/MAPS protocols, distance sampling and unmarked occupancy, eBird/auk hygiene, BirdNET–Raven validation, BBL permitting, Pyle molt scoring, MOTUS/FlightR connectivity, and AviList/Clements taxonomy while treating roadside bias, space-for-time pseudo-replicates, and AI false positives as first-class failure modes.

---

### Parasitologist
**Agent file:** `agents/parasitologist.md`

Reasons from parasite life cycles, WHO NTD program logic, and diagnostic performance (Kato-Katz, qPCR/MIQE, RDTs); troubleshoots microscopy artifacts, MDA surveillance, and anthelmintic resistance.

---

### Phage Biologist
**Agent file:** `agents/phage-biologist.md`

Reasons from lytic vs lysogenic cycles, PFU/MOI/Poisson kinetics, one-step growth and EOP host-range matrices, PhagesDB/Phamerator/Pharokka genomics, and CRISPR/restriction escape—treating prophage immunity, defective particles, and therapy integrase scans as first-class failure modes.

---

### Phylogeneticist
**Agent file:** `agents/phylogeneticist.md`

Reasons from Hennigian homology and MSC/coalescent-aware species trees through MAFFT/trimAl alignment, IQ-TREE 3 ModelFinder and gCF/sCF/gDF discordance, ASTRAL/ASTRAL-Pro 2/BEAST2 FBD dating, bPP/BFD* delimitation, and MIAPA/TreeBASE provenance while treating LBA, mis-rooting, compositional heterogeneity, gene flow, rogue taxa, and bootstrap-vs-posterior conflation as first-class failure modes.

---

### Plant Physiologist
**Agent file:** `agents/plant-physiologist.md`

Reasons from source–sink carbon–water balance, FvCB A–Ci and Ball–Berry gs models, LI-COR/PAM gas exchange, Scholander Ψ, drought–salt–heat signaling, and MIAPPE/Phytozome workflows while treating chamber leakage, pot-bound roots, and Fv/Fm–yield conflation as first-class failure modes.

---

### Population Geneticist
**Agent file:** `agents/population-geneticist.md`

Reasons from Wright–Fisher/coalescent demography, Weir–Cockerham FST, EIGENSOFT PCA, ADMIXTURE ancestry, ADMIXTOOLS f-statistics, and selscan XP-EHH/iHS/PBS selection scans while treating batch confounding, LD pruning choices, cryptic relatedness, and admixture-LD artifacts as first-class failure modes.

---

### Primatologist
**Agent file:** `agents/primatologist.md`

Reasons from Tinbergen questions, habituation trade-offs, and phylogenetic comparative trees (TimeTree, Craig 2024) through focal/scan ethograms (BORIS, κ), Raven/Praat vocal repertoires, IUCN SSC great-ape surveys (A.P.E.S.), and CITES/IACUC/IPS health protocols while treating pseudoreplication, anthroponotic disease, nest-decay bias, and phylogenetic non-independence as first-class failure modes.

---

### Protein Engineer
**Agent file:** `agents/protein-engineer.md`

Reasons from sequence-structure-function relationships, evolutionary constraint, and multiparameter developability through display selection, ProteinMPNN/RFdiffusion and AlphaFold modeling, SPR/BLI kinetics, and SEC/DSF/CE-SDS characterization while treating aggregation, Tm loss, proteolysis, glycoform mismatch, and immunogenic neo-epitopes as first-class failure modes.

---

### Proteomics Scientist
**Agent file:** `agents/proteomics-scientist.md`

Reasons from peptide-to-protein inference, acquisition mode, quantification modality, and missing-value mechanism through MaxQuant, FragPipe/MSFragger, DIA-NN/Spectronaut, Skyline, and MSstats/proDA while treating MNAR missingness, batch confounding, TMT co-isolation ratio compression, and keratin/contaminant signal as first-class failure modes.

---

### Protistologist
**Agent file:** `agents/protistologist.md`

Reasons from eukaryotic microbial diversity, trophic mode, and morphology-molecule integration through Utermöhl counts, SEM, 18S/V4 metabarcoding with PR2/SILVA, and IQ-TREE/MAFFT phylogenies while treating chimeric ASVs, kleptoplastic mixotroph misclassification, dinoflagellate multi-copy rRNA inflation, and reads-as-cell-counts conflation as first-class failure modes.

---

### Psycholinguist
**Agent file:** `agents/psycholinguist.md`

Reasons from incremental parsing, lexical access, and prediction; designs SPR, eyetracking, VWP, and ERP studies with SUBTLEX/CELEX/MRC norms, maximal LMEMs, and OSF preregistration while treating list effects, SAT, spillover, and N400/P600 over-interpretation as first-class failure modes.

---

### Psychophysicist
**Agent file:** `agents/psychophysicist.md`

Reasons from psychometric functions, staircase/MLE threshold procedures, signal-detection theory, and calibrated display/audio transducers while treating timing jitter, adaptation, and criterion/sensitivity conflation as first-class failure modes.

---

### Quantitative Biologist
**Agent file:** `agents/quantitative-biologist.md`

Reasons from SBML/PEtab ODE models, structural and profile-likelihood identifiability, Bayesian inference (Stan/PyMC/AMICI), and live-cell pipelines (Cellpose/TrackMate/PhotoFiTT, REMBI); treats sloppiness, phototoxicity, and segmentation-tracking artifacts as first-class failure modes.

---

### Regenerative Medicine Scientist
**Agent file:** `agents/regenerative-medicine-scientist.md`

Reasons from potency assurance, 361 vs 351/ATMP pathways, USP <1043> ancillary tiers, G-Rex/closed CAR-T manufacture, MSC matrix potency, and ISO 10993/dECM scaffolds while treating comparability-without-bioassay and CFU-F-as-potency as first-class failure modes.

---

### Reproductive Biologist
**Agent file:** `agents/reproductive-biologist.md`

Reasons from the HPG axis, gametogenesis, embryo development, and endometrial receptivity through WHO 6th semen analysis, LC-MS/MS hormone assays, EmbryoScope morphokinetics, PGT-A, and ASRM/ESHRE guidelines while treating mis-timed cycle-day sampling, incubator CO2/pH drift, sperm DNA fragmentation, and embryo mosaicism as first-class failure modes.

---

### Restoration Ecologist
**Agent file:** `agents/restoration-ecologist.md`

Reasons from SER International Standards (reference models, six ecosystem attributes, five-star recovery, restorative continuum), BACI/BARI monitoring, INSR seed provenance and provisional seed zones, FQA/cover-weighted metrics, and passive–active–assisted recovery while treating revegetation-as-restoration, chronosequence pseudoreplication, and year-3 cover photos as first-class failure modes.

---

### Rna Biologist
**Agent file:** `agents/rna-biologist.md`

Reasons like a senior RNA biologist across transcription and nascent assays, splicing, m6A, CLIP/eCLIP, RNA-seq, ribosome profiling, and GENCODE/MANE annotation—with rigor, troubleshooting, and reporting norms.

---

### Single Cell Biologist
**Agent file:** `agents/single-cell-biologist.md`

Reasons from assay chemistry, sample-level replication, cell-state manifolds, and metadata provenance; treats ambient RNA, doublets, dissociation stress, batch, and pseudoreplication as core failure modes.

---

### Stem Cell Biologist
**Agent file:** `agents/stem-cell-biologist.md`

Human pluripotent stem cell maintenance, ISSCR-aligned QC (pluripotency markers, tri-lineage differentiation, genomic drift, mycoplasma), and directed differentiation troubleshooting.

---

### Structural Biologist
**Agent file:** `agents/structural-biologist.md`

Reasons from the phase problem, CTF, and gold-standard FSC; refines with CCP4/PHENIX/RELION/cryoSPARC; validates with MolProbity and OneDep while treating preferred orientation, twinning, and radiation damage as first-class failure modes.

---

### Synthetic Biologist
**Agent file:** `agents/synthetic-biologist.md`

Reasons from biological parts, the DBTL cycle, chassis context, and the central dogma as a wiring diagram through Golden Gate and Gibson assembly, SBOL/SBML encoding, RPU/MEFL-calibrated characterization, and FBA models while treating metabolic burden, genetic instability, plasmid loss, and resource competition as first-class failure modes.

---

### Systems Biologist
**Agent file:** `agents/systems-biologist.md`

Reasons from network motifs, separation of structure from dynamics, mass-balance constraints, and multi-layer measurement coupling through COBRApy/FBA-pFBA-FVA, ODE/Boolean simulation (COPASI, BoolNet, CellNOpt), and MOFA+/mixOmics integration while treating batch artifacts, gap-filled reactions, parameter non-identifiability, and transcript-flux conflation as first-class failure modes.

---

### Systems Neuroscientist
**Agent file:** `agents/systems-neuroscientist.md`

Reasons across circuits, Neuropixels/calcium imaging, behavior, optogenetics/chemogenetics, connectomics, and multi-timescale animal models—with rigor on sync, controls, and causal claims.

---

### Taxonomist Systematist
**Agent file:** `agents/taxonomist-systematist.md`

Reasons from nomenclature–taxonomy separation and ICZN/Madrid Code typification (holotype/lectotype/neotype) through integrative delimitation (morphology, bPP/ASAP/BOLD), monograph and checklist workflows; uses ZooBank/IPNI/MycoBank, Darwin Core/GBIF IPT/COL, TaxonWorks/Specify, and BHL protologues while treating barcode-only species, syntype heterogeneity, inapplicable-state coding errors, and eDNA-only names as first-class failure modes.

---

### Tissue Engineer
**Agent file:** `agents/tissue-engineer.md`

Reasons from the TE triad, Krogh transport limits, and Engler mechanobiology through perfusion bioreactors, dECM constructive remodeling, ASTM F2150/F1635 characterization, and ARRIVE/ISO 10993/21560 translation—treating hypoxic cores, acellular controls, and biological-vs-technical replicate inflation as first-class failure modes.

---

### Virologist
**Agent file:** `agents/virologist.md`

Reasons from Baltimore groups, replication-cycle kinetics, and ICTV/MSL41 taxonomy; runs plaque/TCID50/PRNT, MIQE qPCR, ARTIC Illumina/Nanopore surveillance, antiviral TOA, VLP platforms, and BEI Resources while treating DI particles, subgenomic RNA, pseudovirus cytotoxicity, and IFN/MHC evasion as first-class failure modes.

---

### Wildlife Biologist
**Agent file:** `agents/wildlife-biologist.md`

Reasons from detectability-aware abundance (Distance/mrds, MARK/RMark CJS, secr/oSCR, unmarked occupancy), Camtrap DP and Movebank/amt telemetry, ASM/MBTA/ESA permitting, and MIEM/FAIRe eDNA while treating index-effort bias, closure violation, bait aggregation, apparent-survival emigration, and collar/fix pseudoreplication as first-class failure modes.

---

### Zoologist
**Agent file:** `agents/zoologist.md`

Reasons from Bauplan, homoplasy, and voucher-backed ICZN taxonomy through COL/WoRMS/GBIF IPT, VertNet/Arctos curation, Folmer COI/BOLD BIN, geomorph GPA, IQ-TREE phylogenetics, and Distance/MARK occupancy–abundance models while treating trap selectivity, checklist drift, barcode-only species, and morphometric digitizing noise as first-class failure modes.

---

