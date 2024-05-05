
import os
import json
import pytest

@pytest.fixture(scope="session")
def dataset_file():
    data = {
        'a': 1,
        'b': 2,
    }
    filename = "/tmp/example-123"
    with open(filename, "w") as f:
        json.dump(data, f)

    yield filename
    
    os.remove(filename)
    
def test_hello(dataset_file):
    assert os.path.exists(dataset_file)
    


