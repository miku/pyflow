
import pytest

@pytest.fixture
def dataset():
    return {
        'a': 1,
        'b': 2,
    }

def test_hello(dataset):
    assert 'b' in dataset


