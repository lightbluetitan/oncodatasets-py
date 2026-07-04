"""
oncodatasets
A Python package providing curated collection of oncological, clinical trial, and cancer survival datasets in CSV format from curated R dataset packages.
"""

__version__ = "0.1.0"

from .core import load_dataset, list_datasets, describe
from .datasets import DATASETS

__all__ = [
    "load_dataset",
    "list_datasets",
    "describe",
    "DATASETS",
    "__version__",
]
