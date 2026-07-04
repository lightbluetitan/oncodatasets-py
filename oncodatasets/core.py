from pathlib import Path
import pandas as pd
from .datasets import DATASETS

_DATA_PATH = Path(__file__).parent / "data"


def list_datasets():
    """
    Return a sorted list of available dataset names.
    """
    return sorted(DATASETS.keys())


def describe(name):
    """
    Return metadata for a given dataset.
    """
    if name not in DATASETS:
        raise ValueError(
            f"Dataset '{name}' not found. "
            f"Available datasets: {', '.join(list_datasets())}"
        )
    return DATASETS[name]


def load_dataset(name):
    """
    Load a dataset by name and return a pandas DataFrame.
    """
    if name not in DATASETS:
        raise ValueError(
            f"Dataset '{name}' not found. "
            f"Available datasets: {', '.join(list_datasets())}"
        )
    filename = DATASETS[name]["Filename"]
    file_path = _DATA_PATH / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {filename}")
    return pd.read_csv(file_path, low_memory=False)