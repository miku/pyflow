# Data Oriented Programming

Various topics around working with data.

# Modeling Records

* tuple, namedtuple

# Data Classes

* added in 3.7
* some voices claim, that every class can start as a dataclass - [data-classification](https://blog.glyph.im/2023/02/data-classification.html)

>  Although they use a very different mechanism, Data Classes can be thought of as “mutable namedtuples with defaults”. -- [https://peps.python.org/pep-0557/](https://peps.python.org/pep-0557/)

* uses a decorator
* uses annotations
* allows to set defaults
* avoids boilerplate


> there’s really nothing special about the class: the decorator adds generated methods to the class and returns the same class it was given.

Given a class:

```python
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

The decorator will expand this definition into the following (8 special methods):

```python
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0) -> None:
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
def __repr__(self):
    return f'InventoryItem(name={self.name!r}, unit_price={self.unit_price!r}, quantity_on_hand={self.quantity_on_hand!r})'
def __eq__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) == (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ne__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) != (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __lt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) < (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __le__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) <= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __gt__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) > (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
def __ge__(self, other):
    if other.__class__ is self.__class__:
        return (self.name, self.unit_price, self.quantity_on_hand) >= (other.name, other.unit_price, other.quantity_on_hand)
    return NotImplemented
```


There are a couple of inspirations, where dataclass originates from:


* collections.namedtuple in the standard library (2.6+)
* typing.NamedTuple in the standard library.
* The popular attrs [1] project.
* George Sakkis’ [recordType recipe](https://code.activestate.com/recipes/576555-records/), a mutable data type inspired by collections.namedtuple.
* Many example online recipes [3], packages [4], and questions [5]. David Beazley used a form of data classes as the motivating example in a PyCon 2013 metaclass talk [6].


Parameters of the `dataclass` decorator.

```
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)
```

* "match_args" corresponds to the `match` statement (3.10)


# The attrs project

* inspiration for dataclasses
* not standard library, but more powerful

Some differences to dataclasses:

* has validators, equality customizations, extensibility
* attrs doesn’t force type annotations on you if you don’t like them.

Tradeoff: standard library (moving slow, always available) vs third-party project (moving fast, another dependency)

The attrs project provides:

* a concise and explicit overview of the class’s attributes,
* a nice human-readable __repr__,
* equality-checking methods,
* an initializer,
* and much more,

without writing dull boilerplate code again and again and without runtime performance penalties.

Hate type annotations!? No problem! Types are entirely optional with attrs. Simply assign attrs.field() to the attributes instead of annotating them with types.

Lightweight helper:

> You define a class and attrs adds static methods to that class based on the attributes you declare. The end. It doesn’t add metaclasses. It doesn’t add classes you’ve never heard of to your inheritance tree. An attrs class in runtime is indistinguishable from a regular class: because it is a regular class with a few boilerplate-y methods attached.

If in doubt, the standard library dataclass may be enough.

# Data Validation with Pydantic

* allows to model data, with type annotations

```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Jane Doe'
``` 

Models support a variety of extra methods, e.g. for exporting like `json`,
`dict` or JSON schema. Validation can be circumvented with `construct`.

Examples: [Snippets/Pydantic](Snippets/Pydantic)

