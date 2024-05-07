# Type Hints (2/n)

* Gradually added to Python 3

Defined by various PEPs:

* [483](https://peps.python.org/pep-0483/) -- The Theory of Type Hints (2014)
* [484](https://peps.python.org/pep-0484/) -- Type Hints (2014)

And more [relevant PEPs](https://docs.python.org/3/library/typing.html#relevant-peps):

* [526](https://peps.python.org/pep-0526/) -- Variable Annotations (2016)
* [544](https://peps.python.org/pep-0544/) -- Protocols: Structural subtyping (static duck typing) (2017)
* [585](https://peps.python.org/pep-0585/) -- Type Hinting Generics In Standard Collections (2019)
* [586](https://peps.python.org/pep-0586/) -- Literal Types (2019)
* [589](https://peps.python.org/pep-0589/) -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys (2019)
* [591](https://peps.python.org/pep-0591/) -- Adding a final qualifier to typing (2019)
* [593](https://peps.python.org/pep-0593/) -- Flexible function and variable annotations
* [604](https://peps.python.org/pep-0604/) -- Allow writing union types as X | Y (2019)
* [612](https://peps.python.org/pep-0612/) -- Parameter Specification Variables (2019)
* [613](https://peps.python.org/pep-0613/) -- Explicit Type Alias (2020)
* [647](https://peps.python.org/pep-0647/) -- User-Defined Type Guards (2020)

Other:

* [3107](https://peps.python.org/pep-3107/) -- Function Annotations

> Function annotations, both for parameters and return values, are completely
optional. Function annotations are nothing more than a way of associating
arbitrary Python expressions with various parts of a function at compile-time.

Function annotations are not limited to type hints.

## Annotations

* not limited to type hints, but generic way to annotate function parameters and
  return values (other [use cases](https://peps.python.org/pep-3107/#use-cases))

```python

def hello(greeting: "greeting word", name: "custom name") -> "result":
    return f"{greeting} from {name}"

print(hello("hello", "world"))
print(hello.__annotations__)

# hello from world
# {'greeting': 'greeting word', 'name': 'custom name', 'return': 'result'}

```

## Highlights from PEP-484

> In its basic form, type hinting is used by filling function annotation slots with classes:

A new module is used (e.g. for names None, Any, Union, Tuple, Callable)

> All newly introduced names used to support features described in following
> sections (such as Any and Union) are available in the typing module.


Example callable:

```python
from typing import Callable

def f(g : Callable[..., bool]) -> bool:
    return True
```

```
$ mypy Snippets/TypeHints/call.py
Success: no issues found in 1 source file
```

We can express generics:

```python
from typing import Mapping, Set

def notify_by_email(employees: Set[Employee], overrides: Mapping[str, str]) -> None: ...
```

We can define a Type variable:

```python
from typing import Sequence, TypeVar

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]
```

Type variables can define one or more other types:


> TypeVar supports constraining parametric types to a fixed set of possible
> types (note: those types cannot be parameterized by type variables). For
> example, we can define a type variable that ranges over just str and bytes. By
> default, a type variable ranges over all possible types. Example of
> constraining a type variable:

```python
from typing import TypeVar, Text

AnyStr = TypeVar('AnyStr', Text, bytes)

def concat(x: AnyStr, y: AnyStr) -> AnyStr:
    return x + y
```

Both x and y need to be the *same* type.

> List and List[Any] mean the same

A user defined generic type uses `Generic` type.

```
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('{}: {}'.format(self.name, message))
```

## Generic types

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def  __init__(self, k : T):
        self.k = k

    def __repr__(self):
        return f'{self.k} of type {type(self.k)}'


node = Node(int)
print(node)

node = Node(123)
print(node)
```

## Type Aliases

Support to readability and compact code.

```
from typing import List, Tuple

Book = Tuple[str, str, int]

movies: List[Book] = [
    ("Python", "Andrew", 2005),
    ("Inside Python", "Pete", 2015),
    ("Clean code", "Lee", 2010)
]
```

## Covariance and Contravariance

> covariant. This means that the subtyping relation of the simple types are preserved for the complex types.

i.e. is `List[Cat]` a subclass of `List[Amimal]` -- if so, then the list type contructor is covariant.

## Forward References

> When a type hint contains names that have not been defined yet, that
> definition may be expressed as a string literal, to be resolved later.

## List or list

> In Python 3.9 we won't have to import things like Tuple, List, and Dict from
> the typing module. Instead, we'll be able to use the standard tuple, list, and
> dict types for annotation.


## Union Types

```python
from typing import Union

def handle_employees(e: Union[Employee, Sequence[Employee]]) -> None:
    if isinstance(e, Employee):
        e = [e]
    ...
```

Union type can represent an optional type as well:

```python
def handle_employee(e: Union[Employee, None]) -> None: ...
```

Which got an own shorthand:

```python
from typing import Optional

def handle_employee(e: Optional[Employee]) -> None: ...
```

## Any Type

> A special kind of type is Any. Every type is consistent with Any. It can be
> considered a type that has all values and all methods. Note that Any and
> builtin type object are completely different.

It's the type used implicitly:

> A function parameter without an annotation is assumed to be annotated with Any.


## NoReturn Type

```python
from typing import NoReturn

def stop() -> NoReturn:
    raise RuntimeError('no way')
```

----

## Stub Files


> Stub files are files containing type hints that are only for use by the type
> checker, not at runtime. There are several use cases for stub files:

* Extension modules
* Third-party modules whose authors have not yet added type hints
* Standard library modules for which type hints have not yet been written
* Modules that must be compatible with Python 2 and 3
* Modules that use annotations for other purposes

Generated with:

* [](https://mypy.readthedocs.io/en/stable/stubgen.html)

```python
BORDER_WIDTH = 15

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def create_empty() -> Window:
    return Window(0, 0)


# $ stubgen example.py
#
# $ cat out/example.pyi
# from _typeshed import Incomplete
#
# BORDER_WIDTH: int
#
# class Window:
#     width: Incomplete
#     height: Incomplete
#     def __init__(self, width, height) -> None: ...
#
# def create_empty() -> Window: ...
```


## When to use type checking?

* public APIs, library entry points
* highlight a more complicated piece of logic
* discover bugs and inconsistencies


## A few techniques

Beyond basic annotations, there are a few ways to constrain types.

## Optional

```python
from typing import Optional

string_or_none: Optional[str] = "abc"
```

Optional is a shorthand for Union of `None` and a type.

* helpful hint
* will lead to mypy warnings when e.g. methods are called on an optional type before `None` check

## Union

```python
from typing import Union

def fetch(k:int = 0) -> Union[int, str]:
    if k == 0:
        return 0
    else:
        return "nonzero"
```

* disparate return types
* similar to "Optional", but maybe carrying error messages
* handling different user input
* backwards compatibilty

## Literal

* help to reduce number of valid values

Example: [Snippets/TypeHints](Snippets/TypeHints)

## NewType

* creates a distinct type
* `Derived = NewType('Derived', Base)`

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
```

* can help to model stages of an object

> Maybe we have a setup type that goes to different stages, before it is done.
> We could distinguish the same object during this cycle.

```python
SetupDone = NewType('SetupDone', Setup)
```

## Final

* restrict a type from changing its value


## Collections

* use generic collection annotations
* https://docs.python.org/3/library/typing.html#generic-concrete-collections
* Dict, List, Set, FrozenSet, ...


## Dictionaries

* use [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict) to annotate a dictionary

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
```

* model more complex structures, e.g. api responses




## Other considerations

* try to make invalid states unrepresentable

Example: Split a type carrying both a value and error conditions into two parts.



## Other tools

* pyre
* pysa

> Pyre ships with Pysa, a security focused static analysis tool we've built to
> reason about data flows in Python applications at scale.

Allows to mark tainted code, e.g. a source (user input) and sinks (shell calls)
to check for possible remove code executions.

Input needs to be sanitized, and can be marked manually.

