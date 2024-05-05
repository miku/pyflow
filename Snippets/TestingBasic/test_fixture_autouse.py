
import os
import json
import pytest

@pytest.fixture(autouse=True, scope="session")
def dataset_file():
    data = {
        'a': 1,
        'b': 2,
    }
    with open("/tmp/example-123", "w") as f:
        json.dump(data, f)
    
def test_hello():
    assert os.path.exists('/tmp/example-123')


