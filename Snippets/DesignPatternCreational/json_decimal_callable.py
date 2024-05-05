# Pragmatic "abstract factory", customize object creation inside json
# deserialization by passing a callable to json.loads.
import json
from decimal import Decimal

text = '{"total": 9.61, "items": ["Americano", "Omelet"]}'
print(json.loads(text, parse_float=Decimal))
