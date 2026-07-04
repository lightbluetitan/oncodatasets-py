# oncodatasets – Examples

This page provides practical examples of using `oncodatasets` for data analysis and exploration.

## Basic Examples

### Example 1: Loading and Exploring a Dataset

Learn how to load a dataset and perform basic exploration.

```python
import oncodatasets as ocd

# Load the comparison of two prostate cancer treatments from a Veteran's Administration.
prostate_cancer_001 = ocd.load_dataset("prostate_cancer_treatment")

# Display first few rows
print(prostate_cancer_001.head())

# Check dataset shape
print(f"\nDataset shape: {prostate_cancer_001.shape}")

# View column names
print(f"\nColumns: {list(prostate_cancer_001.columns)}")

# Get summary statistics
print("\nSummary statistics:")
print(prostate_cancer_001.describe())

# Check for missing values
print("\nMissing values:")
print(prostate_cancer_001.isnull().sum())
```

### Example 2: Exploring survival data for thirty-five women with stage II and IIA ovarian carcinoma.

```python
import oncodatasets as ocd

ovarian_carcinoma_001 = ocd.load_dataset("ovarian_carcinoma_stage")
print(ovarian_carcinoma_001.head())
print(f"\nDataset shape: {ovarian_carcinoma_001.shape}")
print(f"\nColumns: {list(ovarian_carcinoma_001.columns)}")
```

### Example 3: Listing all available datasets

```python
import oncodatasets as ocd

datasets = ocd.list_datasets()
print(datasets)
```