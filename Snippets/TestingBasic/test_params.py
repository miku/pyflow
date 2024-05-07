import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, result", [
    (1, 1, 2),
    (1, 2, 4),
])
def test_add(a, b, result):
    assert add(a, b) == result
    # ...