# oncodatasets Documentation

## Welcome

The `oncodatasets` package provides a curated collection of oncological, clinical trial,
and cancer survival datasets for data analysis, statistical modeling, and machine learning
research. It includes datasets related to **breast, lung, ovarian, prostate, bladder,
colorectal, gastric, and cervical cancer diagnostics and survival analysis, tumor gene
expression profiles, dose-response carcinogen experiments in laboratory animals,
patient-reported quality of life (QoL) metrics, and epidemiological cancer incidence and
mortality rates**.

The package contains datasets related to breast cancer FNA biopsy features, leukemia and
lymphoma survival records, BRCA1/BRCA2 mutation risk estimates, prostate-specific antigen
(PSA) biomarker measurements, bone marrow transplantation outcomes, glioma
radioimmunotherapy trials, and much more from curated R packages on CRAN.


### Philosophy

The author's vision is to create **specialized dataset packages** focused on specific
themes and topics. Instead of searching through multiple generic data packages to find
relevant datasets, users can go directly to a thematic package where all datasets are
carefully curated around a particular subject.

In the case of `oncodatasets`, every dataset is **exclusively focused on oncological,
clinical trial, and cancer survival research**, making it the go-to resource for
researchers, data scientists, statisticians, oncologists, epidemiologists, and students
working in the fields of oncology, biostatistics, epidemiology, clinical research,
and machine learning.

## Getting Started

### Installation

#### From PyPI (Recommended)

The easiest way to install `oncodatasets` is directly from PyPI:

```bash
pip install oncodatasets
```

#### From GitHub (Latest Development Version)

To get the latest development version with the newest features and bug fixes:

```bash
pip install git+https://github.com/lightbluetitan/oncodatasets-py
```

### Quick Start Tutorial

#### 1. Import the Package

```python
import oncodatasets as ocd
```

#### 2. List Available Datasets

See all datasets included in the package:

```python
# Get list of all datasets
datasets = ocd.list_datasets()
print(datasets)
```

#### 3. Load a Dataset

Load any dataset as a pandas DataFrame:

```python
# Load breast_lymph_node
df = ocd.load_dataset('breast_lymph_node')

# Display first rows
print(df.head())

# Check dataset dimensions
print(f"Shape: {df.shape}")
```

#### 4. Describe a dataset

```python
# Describe a dataset
print(ocd.describe("brain_cancer"))
```

### Basic Concepts

#### Dataset Naming Convention

All dataset names in `oncodatasets` follow a consistent naming pattern:

- Lowercase with underscores: `brain_cancer`
- Descriptive names that reflect content


#### Some Datasets available at `oncodatasets`

Every dataset is **exclusively focused on oncological, clinical trial, cancer survival datasets and related topics for
data analysis, statistical modeling, and machine learning**:

- **prostate_cancer_treatment**: Comparison of two prostate cancer treatments from a Veteran's Administration randomized controlled trial.
- **pulmonary_metastasis**: Pulmonary metastasis times with no censoring.
- **glioma_radioimmunotherapy**: Glioma patient data from a yttrium-90-biotin radioimmunotherapy pilot study.
- **ovarian_carcinoma_stage**: Survival data for thirty-five women with stage II and IIA ovarian carcinoma.
- **leukemia_bone_marrow**: Bone marrow transplantation in the treatment of leukemia.

> **Disclaimer:** The datasets included in `oncodatasets` are provided strictly for
> educational, research, and informational purposes. 
> For cancer diagnosis, treatment decisions, or any clinical or healthcare-related
> decision-making, always consult a qualified oncologist or healthcare professional.

#### Data Licenses

All datasets are sourced from the R package ecosystem (CRAN) and maintain their
original open-source licenses:

- Most datasets use **GPL (>= 2)**, **GPL-2**, or **GPL-3**
- Some use **MIT + file LICENSE**
- The `oncodatasets` package itself is licensed under **GNU General Public License v3 or later (GPLv3+)**