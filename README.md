# Alzheimer's Disease Blood-Based Molecular Subtyping and Classification

**Author**: Collin McNeil
**Course**: BIN602: Data Mining for Bioinformatics
**Date**: Jan 2026

## Research Questions

### Primary Questions

1. **Disease Classification & Biomarker Discovery**
    Can we accurately predict Alzeimer's disease status from blood gene expression profiles, and which genes are the most informative biomarkers?

2. **Disease Subtype Discovery**  
    Are there distinct molecular subtypes of Alzheimer's disease patients identifiable through unsupervised clustering of blood gene expression patterns?

3. **Integrated Approach**
    Do molecularly-defined patient subtypes (from clustering) show different classification accuracy, and does subtype-aware modeling improve prediction performance?

## Dataset

**Source**: Gene Expression Omnubus (GEO)
**Accession**: GSE48350
**Title**: Alzheimer's Disease Dataset
**Link**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE48350
**Sample Size**: 253 samples (AD patients and healthy controls)

## Data Files 

After running the download script, your `data/` directory will contain:
- `GSE48360_series_matrix.txt` - Expression data and metadata
- Processed files generated during analysis (these are not committed to Git)

**Note**: Raw data files are not committed to this repository due to size. Run the download script to scrape them.

## Analysis Overview

The analysis is as follows:

1. **Data Loading & Preprocessing**
- Load expression data from GEO
- Extract sample metadata
- Quality control and filtering

2. **Exploratory Data Analysis**
- Distribution analysis
- PCA visualization
- Sample clustering

3. **Unsupervised Learning (Clustering)**
- K-means clustering
- Hierarchical clustering
- Cluster characterization

4. **Supervised Learning (Classification)**
- Random Forest classifier
- Support Vector Machine
- Feature importance analysis

5. **Integrated Analysis**
- Subtype-specific classification
- Performance comparison
- Biomarker identification

## Results

[Add after analysis]

## References

- GEO Dataset: Sood S, et al. (2015) "A novel multi-tissue RNA diagnostic of healthy ageing relates to cognitive health status." Genome Biology.