# Creational Patterns

## Abstract Factory

* standard library has almost no factories (when grepping for "Factory") - and if, then mostly in test cases
* even collections.abc is relatively rare

Observation:

> The Abstract Factory is an awkward workaround for the lack of first-class
> functions and classes in less powerful programming languages. It is a poor
> fit for Python, where we can instead simply pass a class or a factory
> function when a library needs to create objects on our behalf. -- [https://python-patterns.guide/gang-of-four/abstract-factory/](https://python-patterns.guide/gang-of-four/abstract-factory/)

Both functions and class can be passed around. A class can be a callable.

Sometime, the "factory" shrinks to a parameter with some sensible default, e.g.
like in [json.loads](https://docs.python.org/3/library/json.html#json.loads).

```
import json
from decimal import Decimal

def build_decimal(string):
    return Decimal(string)

print(json.loads(text, parse_float=build_decimal))
```

## Builder

## Factory Method

## Prototype

## Singleton

