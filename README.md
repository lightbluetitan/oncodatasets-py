# oncodatasets

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The `oncodatasets` package provides a curated collection of oncological, clinical trial, and cancer
survival datasets for data analysis, statistical modeling, and machine learning research. Includes breast
cancer diagnostics, lung and bladder cancer survival analysis, tumor gene expression profiles,
dose-response carcinogen experiments in laboratory animals, patient-reported quality of life (QoL)
metrics, epidemiological incidence and mortality rates, and clinical trial outcomes from curated
R packages on CRAN.


## Installation
You can install the `oncodatasets` package from PyPI:
```bash
pip install oncodatasets
```

## Usage
```python

import oncodatasets as ocd

# List all available datasets

datasets = ocd.list_datasets()
print(datasets)

# Load a specific dataset

df = ocd.load_dataset('brain_cancer')
print(df.head())

# Describe dataset

df_01 = ocd.describe('brain_cancer')
print(df_01)

```

## 📊 Some Available Datasets

| Dataset | Description |
|---------|-------------|
| `breast_cancer_diagnostic` | Features from digitized FNA images of breast masses from Wisconsin Hospitals. |
| `lip_cancer_scotland` | Observed and expected lip cancer cases across 56 Scottish counties (1975–1980). |
| `cancer_dogs` | Case-control study data (1994) on herbicide exposure and cancer risk in dogs. |


> Run `oncodatasets.list_datasets()` or `ocd.list_datasets()` (using `ocd` as alias) to see the full list of available datasets.

## Disclaimer

The datasets included in `oncodatasets` are provided strictly for educational,
research, and informational purposes. All datasets originate from curated R packages
available on CRAN and retain their original licenses and attributions.

The author of `oncodatasets` makes no warranties, express or implied, regarding
the accuracy, completeness, or suitability of any dataset for a particular purpose.
Users are solely responsible for ensuring that their use of these datasets complies
with applicable laws, regulations, and ethical guidelines.

Any findings, conclusions, or decisions derived from the use of these datasets
are the sole responsibility of the user. The author shall not be held liable for
any direct, indirect, incidental, or consequential damages arising from the use
or misuse of the datasets included in this library.

For clinical, diagnostic, or any medical decision-making purposes, always consult
a qualified healthcare professional or oncologist.


## License

The `oncodatasets` library is released under the **GNU General Public License v3 (GPLv3)**, which ensures that all source code and derived data works remain free and open-source.
See the [LICENSE](LICENSE) file for details.