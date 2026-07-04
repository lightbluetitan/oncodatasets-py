"""
Basic usage example for oncodatasets

Run:
    python basic_usage.py
"""

import oncodatasets as ocd

print("=== oncodatasets: Basic Usage Example ===\n")

# 1. List all available datasets first
print("Available datasets:")
print(ocd.list_datasets())
print("-" * 40)

# 2. Load a dataset
print("Loading 'prostate_cancer_treatment' dataset...")
prostate_cancer_001 = ocd.load_dataset("prostate_cancer_treatment")

# Show basic information (Using native Pandas methods)
print("\nFirst 5 rows:")
print(prostate_cancer_001.head())

print("\nDataset shape:")
print(prostate_cancer_001.shape)

print("\nColumn names:")
print(list(prostate_cancer_001.columns))
print("-" * 40)

# 3. Load another dataset
print("\nLoading 'ovarian_carcinoma_stage' dataset...")
ovarian_carcinoma_001 = ocd.load_dataset("ovarian_carcinoma_stage")

print("\nFirst 5 rows:")
print(ovarian_carcinoma_001.head())
print("-" * 40)

# 4. Describe dataset provenance (Library Metadata)
print("\nDataset Package Metadata & Origin:")
print(ocd.describe("ovarian_carcinoma_stage"))  # Fixed to the correct internal name

print("\nDone.")