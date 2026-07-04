import pandas as pd
import pytest
from oncodatasets.core import list_datasets, load_dataset, describe

def test_list_datasets_returns_list():
    datasets = list_datasets()
    assert isinstance(datasets, list)

def test_list_datasets_not_empty():
    datasets = list_datasets()
    assert len(datasets) > 0

def test_list_datasets_sorted():
    datasets = list_datasets()
    assert datasets == sorted(datasets)

def test_load_dataset_returns_dataframe():
    name = list_datasets()[0]
    df = load_dataset(name)
    assert isinstance(df, pd.DataFrame)

def test_load_dataset_invalid_name():
    with pytest.raises(ValueError):
        load_dataset("this_dataset_does_not_exist")

def test_load_dataset_file_not_found(monkeypatch):
    """
    Test that FileNotFoundError is raised when the CSV file doesn't exist.
    """
    from pathlib import Path
    valid_dataset = list_datasets()[0]

    def mock_exists(self):
        return False

    monkeypatch.setattr(Path, "exists", mock_exists)
    with pytest.raises(FileNotFoundError, match="Dataset file not found"):
        load_dataset(valid_dataset)

def test_describe_returns_dict():
    name = list_datasets()[0]
    result = describe(name)
    assert isinstance(result, dict)

def test_describe_has_required_fields():
    name = list_datasets()[0]
    result = describe(name)
    required_fields = {"Filename","Original name", "Original R package", "Repository", "License", "Description"}
    assert required_fields.issubset(result.keys())

def test_describe_invalid_name():
    with pytest.raises(ValueError):
        describe("this_dataset_does_not_exist")