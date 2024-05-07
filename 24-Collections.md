# Collections

The collections module offers a variety of utility types.

* [notebooks/Collections.ipynb](notebooks/Collections.ipynb)
* [notebooks/CollectionsABC.ipynb](notebooks/CollectionsABC.ipynb)

## Default dictionary

The standard library has many special purpose utilities.

```python

freq = {}

for char in ("a", "b", "c", "b", "c", "c"):
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 0
```

A more compact way to write this would be a default dictionary.

```python

import collections

freq = collections.defaultdict(int)
for char in ("a", "b", "c", "b", "c", "c"):
    freq[char] += 1
```

There is also a `collections.Counter` which is a default dictionary with int
values and a helper method: `most_common`.

## Records with namedtuples

If you have structured information, like a record, consider using a `namedtuple`
or a dataclass.

* tuple
* namedtuple
* dataclass (supplies basic special methods like `str`, allows default values,
  metadata and more)

```python
from dataclasses import dataclass

@dataclass()
class Point:
     x: int
     y: int


p = Point(2, 3)

print(p)
```

* anytime you use a tuple and you are repeatedly accessing by index, you can look into a namedtuple
* simpler than a DataClass
* a factory function, builds a subclass of `tuple`
* interchangable with tuples

Example: [Snippets/Namedtuple]

## Typed named tuples

Example: [Snippets/TypedNamedTuple]


## Related: Data Classes

Data Classes allow to group values, type annotate them.

```python
from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=False)
class Point:
     x: int
     y: int


p = Point(2, 3)

print(p)
```

* Examples: [Snippets/Dataclass](Snippets/Dataclass)

## Map for working with missing keys: defaultdict

* defaultdict provides for a facility to set a dictionaries default value type (e.g. a list)

```
>>> dd = collections.defaultdict(list)
>>> dd["ids"].append(1)
>>> dd["ids"].append(2)
>>> print(dd)
defaultdict(<class 'list'>, {'ids': [1, 2]})
```


## Counter

* a dictionary subclsas that helps to keep track of counting
* came out of a typical use case

```python
>>> c = collections.Counter()
>>> c["a"] += 2
>>> c["b"] += 3
>>> c.most_common()
[('b', 3), ('a', 2)]
```

# Task: A case for collections


Write a short program that given a string, e.g.  like this

```python
s = """
From the Python Website: Python is a high-level, general-purpose programming
language. Its design philosophy emphasizes code readability with the use of
significant indentation. 
"""

# ...

```

[...] collects basic metrics over the text:

* count how often each word (as is, no need to normalize) appears
* collect long words (e.g. 11 chars or longer)

It can output the following:

* top 3 most common words
* a random sample (e.g. of 3) of the longest words

```
the 2
Python 2
From 1

long words: ['readability', 'high-level,', 'indentation.']
```