import pandas as pd

metadata = pd.read_csv('./data/sample_metadata.csv')

# Check if missing Braak/APOE/MMSE are controls
print("Samples WITH Braak stage info:")
has_braak = metadata[metadata['braak stage'].notna()]
print(f"Count: {len(has_braak)}")
print(f"Sample titles (first 5):\n{has_braak['title'].head()}\n")

print("\nSamples WITHOUT Braak stage info:")
no_braak = metadata[metadata['braak stage'].isna()]
print(f"Count: {len(no_braak)}")
print(f"Sample titles (first 5):\n{no_braak['title'].head()}\n")

# Check brain regions for both groups
print("\nBrain regions in samples WITH Braak:")
print(has_braak['brain region'].value_counts())
print("\nBrain regions in samples WITHOUT Braak:")
print(no_braak['brain region'].value_counts())