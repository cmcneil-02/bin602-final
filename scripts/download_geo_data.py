"""
Download and prepare GSE48350 data from GEO

Author: Collin McNeil
Purpose: Download Alzheimer's disease brain gene expression data from GEO
Date: January 2026

Dataset Structure:
- 253 total samples
- 80 AD samples (with Braak stage, MMSE, APOE genotype)
- 173 Control samples (healthy controls without disease metrics)
"""
import GEOparse
import pandas as pd
import os

def download_geo_data(accession="GSE48350", destdir="./data"):
    """
    Download GEO dataset and save to data directory
    
    Parameters:
    -----------
    accession : str
        GEO accession number
    destdir : str
        Destination directory for downloaded files
    """
    print(f"Downloading {accession} from GEO...")
    
    # Download the dataset
    gse = GEOparse.get_GEO(geo=accession, destdir=destdir)
    
    print(f"\nDataset Info:")
    print(f"Number of samples: {len(gse.gsms)}")
    print(f"Platforms: {list(gse.gpls.keys())}")
    
    # Extract sample metadata
    metadata = []
    for gsm_name, gsm in gse.gsms.items():
        sample_info = {
            'sample_id': gsm_name,
            'title': gsm.metadata.get('title', [''])[0],
        }
        # Extract characteristics
        characteristics = gsm.metadata.get('characteristics_ch1', [])
        for char in characteristics:
            if ':' in char:
                key, value = char.split(':', 1)
                sample_info[key.strip()] = value.strip()
        metadata.append(sample_info)
    
    metadata_df = pd.DataFrame(metadata)
    print(f"\nSample metadata shape: {metadata_df.shape}")
    print(f"Metadata columns: {list(metadata_df.columns)}")
    
    # Save metadata
    metadata_path = os.path.join(destdir, "sample_metadata.csv")
    metadata_df.to_csv(metadata_path, index=False)
    print(f"\nMetadata saved to: {metadata_path}")
    
    return gse, metadata_df

if __name__ == "__main__":
    gse, metadata = download_geo_data()
    print("\nDownload complete!")