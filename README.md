# Alzheimer's Disease Brain Gene Expression Analysis: Classification and Molecular Subtyping

**Author:** Collin McNeil    
**Course:** BIN602: Data Mining for Bioinformatics    
**Date:** January 2026    

## Research Questions

### Primary Questions

1. **Binary Disease Classification**  
   Can we accurately distinguish Alzheimer's disease from healthy controls using brain gene expression, and which genes are the most discriminative biomarkers?

2. **Disease Severity Prediction**  
   Among Alzheimer's patients, can we predict disease severity (Braak stage) from gene expression profiles?

3. **Molecular Subtyping**  
   Are there distinct molecular subtypes within Alzheimer's patients that correlate with disease severity, APOE genotype, or brain region?

### Secondary Questions

4. Can we predict cognitive decline (MMSE scores) from gene expression in AD patients using regression?
5. How do gene expression signatures differ between binary classification (AD vs Control) and severity prediction (within AD)?
6. Does APOE genotype influence gene expression patterns and disease classification accuracy?

## Dataset

**Source**: Gene Expression Omnibus (GEO)  
**Accession**: GSE48350  
**Title**: Gene expression in post-mortem brain tissue from Alzheimer's disease patients and healthy controls  
**Link**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48350  
**Platform**: Affymetrix Human Genome U133 Plus 2.0 Array

### Sample Composition
- **Total Samples**: 253
  - **Alzheimer's Disease**: 80 samples
  - **Healthy Controls**: 173 samples
- **Tissue Type**: Post-mortem brain tissue from four regions:
  - Superior frontal gyrus
  - Hippocampus
  - Entorhinal cortex
  - Post-central gyrus

### Available Metadata

**For All Samples**:
- Brain region
- Age
- Gender

**For AD Samples Only**:
- **Braak Stage**: Neuropathological staging (I, II, III, IV, V, VI, V-VI)
- **MMSE Score**: Mini-Mental State Examination (cognitive function, 0-30)
- **APOE Genotype**: Apolipoprotein E genotype (major AD risk factor)

## Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/cmcneil-02/bin602-final.git
cd bin602-final
```

### 2. Install required packages
```bash
pip install GEOparse pandas numpy scikit-learn matplotlib seaborn jupyter scipy
```

### 3. Download the data

Run the download script to fetch GSE48350 from GEO:
```bash
python scripts/download_geo_data.py
```

This downloads the raw data and generates `data/sample_metadata.csv`.

### 4. Clean the metadata

Run the cleaning script to prepare the data for analysis:
```bash
python scripts/clean_metadata.py
```
**Optional**: Run exploratory scripts for quick data checks:
```bash
python scripts/quick_exploration.py
python scripts/further_exploration.py
```

This generates `data/sample_metadata_clean.csv` with:
- Disease status labels (AD vs Control)
- Standardized brain region names
- Filtered and validated Braak stages and MMSE scores

### 5. Run the analysis

Open and run the Jupyter notebook:
```bash
jupyter notebook notebooks/analysis.ipynb
```

## Data Files

After running the setup scripts, your `data/` directory will contain:

- `GSE48350_family.soft.gz` - Raw GEO data (not committed to Git)
- `sample_metadata.csv` - Raw metadata extracted from GEO
- `sample_metadata_clean.csv` - Cleaned and processed metadata ready for analysis

**Note:** Large data files are not committed to this repository. Run the download and cleaning scripts to generate them locally.

## Analysis Overview

The analysis proceeds in the following steps:

### 1. Data Loading & Preprocessing
- Load expression data from GEO
- Clean and validate metadata
- Quality control and normalization

### 2. Exploratory Data Analysis
- Sample distribution by disease status and brain region
- PCA visualization of AD vs Control samples
- Correlation analysis of clinical variables

### 3. Binary Classification (AD vs Control)
- Use all 253 samples
- Compare multiple classifiers (Random Forest, SVM, Logistic Regression)
- Identify top discriminative genes
- Evaluate with cross-validation

### 4. Within-AD Analysis (80 AD samples)
- **Clustering:** Identify molecular subtypes
- **Multi-class classification:** Predict Braak stage
- **Regression:** Predict MMSE scores
- Validate clusters against APOE genotype and brain regions

### 5. Integrated Analysis
- Compare gene signatures from binary vs severity classification
- Analyze subtype-specific progression patterns
- Brain region-specific analysis
- APOE stratification

### 6. Results & Discussion
- Model performance comparison
- Biological interpretation of findings
- Clinical implications

## References

- GEO Dataset: [GSE48350](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48350)
- Braak Staging: Braak H, Braak E. (1991) Neuropathological stageing of Alzheimer-related changes. *Acta Neuropathologica*.