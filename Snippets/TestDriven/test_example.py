# def hello(name=None):
#     return "hello world"


def test_hello():
    assert hello(name="world") == "hello world"
