# Creational Patterns

## Abstract Factory

Definition: The abstract factory pattern in software engineering is a design
pattern that provides a way to create **families of related objects** without
imposing their concrete classes, by encapsulating a group of individual
factories that have a common theme without specifying their concrete classes. -- [https://en.wikipedia.org/wiki/Abstract_factory_pattern](https://en.wikipedia.org/wiki/Abstract_factory_pattern)

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

```python
import json
from decimal import Decimal

def build_decimal(string):
    return Decimal(string)

print(json.loads(text, parse_float=build_decimal))
```

* other example: `SetEncoder`, [json_set_encoder.py](json_set_encoder.py)

Improvement over `json_decimal.py` by removing the extra function and use the `Decimal` class as a callable.

```
# Pragmatic "abstract factory", customize object creation inside json
# deserialization by passing a callable to json.loads.
import json
from decimal import Decimal

text = '{"total": 9.61, "items": ["Americano", "Omelet"]}'
print(json.loads(text, parse_float=Decimal))
```

## Builder

Definition: The builder pattern is a design pattern designed to provide a
flexible solution to various object creation problems in object-oriented
programming. -- [https://en.wikipedia.org/wiki/Builder_pattern](https://en.wikipedia.org/wiki/Builder_pattern)

Use it:

* when the algorithm for creating a complex object should be independent of the
  parts that make up the object and how they are assembled

Some languages do not have default function parameters.

```
adapter = new Adapter("http://example.com/v0", "C", 1, nil, nil, true, "not found");
```

Here, it would be better to write something like:

```
adapter = Builder.withHost("http://example.com/v0")
                 .withCategory("C")
                 .withMaxPerSecond(1)
                 .withExpandedFields(true)
                 .withDefaultMessage("not found");
```

Related SO:
[https://stackoverflow.com/questions/11977279/builder-pattern-equivalent-in-python](https://stackoverflow.com/questions/11977279/builder-pattern-equivalent-in-python),
it says, simply: "Builder pattern not needed"





## Factory Method

Definition:

## Prototype

Definition:

## Singleton

Definition:

