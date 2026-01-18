"""
Clean and prepare GSE48350 metadata for analysis

Author: Collin McNeil
Purpose: Clean metadata, create disease labels, standardize brain regions,
         and prepare data for downstream analysis
Date: January 2026
"""

import pandas as pd
import numpy as np
import os


def clean_metadata(input_path="./data/sample_metadata.csv",
                   output_path="./data/sample_metadata_clean.csv"):
    """
    Clean and prepare metadata for analysis
    
    Parameters:
    -----------
    input_path : str
        Path to raw metadata CSV
    output_path : str
        Path to save cleaned metadata CSV
    
    Returns:
    --------
    pd.DataFrame
        Cleaned metadata dataframe
    """
    
    print("Loading raw metadata...")
    metadata = pd.read_csv(input_path)
    print(f"Initial samples: {len(metadata)}")
    
    # 1. Create disease status label
    print("\n1. Creating disease status labels...")
    metadata['disease_status'] = metadata['title'].str.contains('_AD_', na=False)
    metadata['disease_status'] = metadata['disease_status'].map({True: 'AD', False: 'Control'})
    
    ad_count = (metadata['disease_status'] == 'AD').sum()
    control_count = (metadata['disease_status'] == 'Control').sum()
    print(f"   AD samples: {ad_count}")
    print(f"   Control samples: {control_count}")
    
    # 2. Standardize brain region names
    print("\n2. Standardizing brain region names...")
    brain_region_mapping = {
        'PostcentralGyrus': 'post-central gyrus',
        'postcentral gyrus': 'post-central gyrus',
        'SuperiorFrontalGyrus': 'superior frontal gyrus',
        'Hippocampus': 'hippocampus',
        'EntorhinalCortex': 'entorhinal cortex'
    }
    
    metadata['brain_region_clean'] = metadata['brain region'].replace(brain_region_mapping)
    print("   Unique brain regions after cleaning:")
    print(metadata['brain_region_clean'].value_counts())
    
    # 3. Clean Braak stage
    print("\n3. Cleaning Braak stage...")
    # Keep original braak stage, create a cleaned version
    metadata['braak_stage_clean'] = metadata['braak stage'].copy()
    
    # Handle 'V-VI' - convert to 'V' (conservative choice) or could use 'VI'
    metadata.loc[metadata['braak_stage_clean'] == 'V-VI', 'braak_stage_clean'] = 'V'
    
    # Replace 'no info' with NaN
    metadata.loc[metadata['braak_stage_clean'] == 'no info', 'braak_stage_clean'] = np.nan
    
    # For controls, Braak stage should be NaN (not applicable)
    valid_braak = metadata[metadata['braak_stage_clean'].notna()]
    print(f"   Samples with valid Braak stage: {len(valid_braak)}")
    print(f"   Braak stage distribution:")
    print(valid_braak['braak_stage_clean'].value_counts().sort_index())
    
    # 4. Clean MMSE scores
    print("\n4. Cleaning MMSE scores...")
    metadata['mmse_clean'] = metadata['mmse'].copy()
    
    # Replace 'no info' with NaN
    metadata.loc[metadata['mmse_clean'] == 'no info', 'mmse_clean'] = np.nan
    
    # Convert to numeric
    metadata['mmse_clean'] = pd.to_numeric(metadata['mmse_clean'], errors='coerce')
    
    valid_mmse = metadata[metadata['mmse_clean'].notna()]
    print(f"   Samples with valid MMSE: {len(valid_mmse)}")
    print(f"   MMSE range: {valid_mmse['mmse_clean'].min()} - {valid_mmse['mmse_clean'].max()}")
    print(f"   MMSE mean: {valid_mmse['mmse_clean'].mean():.2f}")
    
    # 5. Clean APOE genotype
    print("\n5. Cleaning APOE genotype...")
    # APOE is only available for AD samples - this is correct
    valid_apoe = metadata[metadata['apoe genotype'].notna()]
    print(f"   Samples with APOE data: {len(valid_apoe)}")
    print(f"   APOE distribution:")
    print(valid_apoe['apoe genotype'].value_counts())
    
    # 6. Convert age to numeric
    print("\n6. Converting age to numeric...")
    metadata['age_numeric'] = pd.to_numeric(metadata['age (yrs)'], errors='coerce')
    print(f"   Age range: {metadata['age_numeric'].min()} - {metadata['age_numeric'].max()}")
    
    # 7. Create analysis subsets flags
    print("\n7. Creating analysis subset flags...")
    
    # Flag for binary classification (all samples)
    metadata['include_binary_classification'] = True
    
    # Flag for severity prediction (AD samples with valid Braak)
    metadata['include_severity_prediction'] = (
        (metadata['disease_status'] == 'AD') & 
        (metadata['braak_stage_clean'].notna())
    )
    
    # Flag for MMSE regression (AD samples with valid MMSE)
    metadata['include_mmse_regression'] = (
        (metadata['disease_status'] == 'AD') & 
        (metadata['mmse_clean'].notna())
    )
    
    # Flag for clustering (all AD samples)
    metadata['include_clustering'] = (metadata['disease_status'] == 'AD')
    
    print(f"   Binary classification: {metadata['include_binary_classification'].sum()} samples")
    print(f"   Severity prediction: {metadata['include_severity_prediction'].sum()} samples")
    print(f"   MMSE regression: {metadata['include_mmse_regression'].sum()} samples")
    print(f"   Clustering: {metadata['include_clustering'].sum()} samples")
    
    # 8. Save cleaned metadata
    print(f"\n8. Saving cleaned metadata to {output_path}...")
    metadata.to_csv(output_path, index=False)
    print("   Done!")
    
    # 9. Summary statistics
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    print(f"Total samples: {len(metadata)}")
    print(f"\nDisease status:")
    print(metadata['disease_status'].value_counts())
    print(f"\nBrain regions:")
    print(metadata['brain_region_clean'].value_counts())
    print(f"\nGender distribution:")
    print(metadata['gender'].value_counts())
    print(f"\nMissing values in key columns:")
    print(metadata[['braak_stage_clean', 'mmse_clean', 'apoe genotype', 
                     'age_numeric']].isnull().sum())
    
    return metadata


if __name__ == "__main__":
    # Check if input file exists
    if not os.path.exists("./data/sample_metadata.csv"):
        print("Error: ./data/sample_metadata.csv not found!")
        print("Please run scripts/download_geo_data.py first.")
        exit(1)
    
    # Clean the metadata
    cleaned_metadata = clean_metadata()
    
    print("\n" + "="*60)
    print("Metadata cleaning complete!")
    print("Cleaned file saved to: ./data/sample_metadata_clean.csv")
    print("="*60)