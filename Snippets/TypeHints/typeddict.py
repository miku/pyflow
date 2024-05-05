from typing import TypedDict

class Range(TypedDict):
    min: float
    max: float
    

class Payload(TypedDict):
    value: int
    unit: str
    range: Range


data = Payload({"value": "x", "unit": "m", "range": {"min": 0.0, "max": 1.0}})

# typeddict.py:14: error: Incompatible types (expression has type "str", TypedDict item "value" has type "int")
# Found 1 error in 1 file (checked 1 source file)


def process_response(response: Payload):
    print(response)
    

process_response(data)
