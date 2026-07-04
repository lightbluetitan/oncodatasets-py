from oncodatasets.datasets import DATASETS

def test_datasets_is_dict():
    assert isinstance(DATASETS, dict)

def test_datasets_not_empty():
    assert len(DATASETS) > 0

def test_each_dataset_has_required_fields():
    required_fields = {"Filename","Original name", "Original R package", "Repository", "License", "Description"}
    for name, meta in DATASETS.items():
        assert isinstance(name, str)
        assert isinstance(meta, dict)
        assert required_fields.issubset(meta.keys())