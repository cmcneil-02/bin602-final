import pandas as pd

# Load metadata
metadata = pd.read_csv('./data/sample_metadata.csv')

# Explore the data
print("Sample size:", len(metadata))
print("\nBraak stage distribution:")
print(metadata['braak stage'].value_counts().sort_index())
print("\nBrain regions:")
print(metadata['brain region'].value_counts())
print("\nAPOE genotypes:")
print(metadata['apoe genotype'].value_counts())
print("\nMMSE summary:")
print(metadata['mmse'].describe())
print("\nMissing values:")
print(metadata.isnull().sum())