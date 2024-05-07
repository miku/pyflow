
import os
import json
import pytest
import random

@pytest.fixture(scope="session")
def dataset_file():
    data = {
        'a': 1,
        'b': 2,
    }
    filename = f"/tmp/example-123-{random.randint(0, 1000)}"
    with open(filename, "w") as f:
        json.dump(data, f)

    yield filename
    
    os.remove(filename)
    
def test_hello(dataset_file):
    print(dataset_file)
    assert os.path.exists(dataset_file)
    
def test_other(dataset_file):
    print(dataset_file)
    assert os.path.exists(dataset_file)
