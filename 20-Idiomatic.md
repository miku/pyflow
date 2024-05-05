# Idiomatic Python

# Pythonic Code

The zen of Python says:

> There should be one-- and preferably only one --obvious way to do it.

There are often different approaches possible.

## EAFP

* easier to ask for forgiveness than permission

```python
try:
    data = float(value)
except ValueError:
    print("not a float")
```

## Indexed iteration

* Python has the builtin `enumerate` for that

```python
i = 0
for v in values:
    i += 1
    print(i, v)
```

The pythonic way to write this would be:

```python
for i, v in enumerate(values):
    print(i, v)
```

----

> Tour: Magic Methods

* [notebooks/Magic_Methods_Part_1.ipynb](notebooks/Magic_Methods_Part_1.ipynb)
* [notebooks/Magic_Methods_Part_2.ipynb](notebooks/Magic_Methods_Part_2.ipynb)

----

## Decorators

* decorators allow to factor out certain cross-cutting concerns
* they are used as an integration tool (e.g. joining routes of a web application with handlers)
* they work, because python has first class functions

Examples:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

* more examples: [https://wiki.python.org/moin/PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)

### Writing a decorator

A decorator is syntactic sugar for:

```python

@decorator
def some_function():
    pass

some_function = decorator(some_function)
```

The main idea is to return a function, that wraps the original function.

* [Snippets/Decorator](Snippets/Decorator)

```python
def deco(f):
    def inner(*args, **kwargs):
        print("[deco] calling {}".format(f.__name__))
        result = f(*args, **kwargs)
        print("[deco] exited {}".format(f.__name__))
        return result
    return inner

@deco
def hello(name="world"):
    print("hello " + name)

hello()
```

## Protocols

One strength of Python is its ability to blend the core language with custom
code. Your object can behave similarly to a sequence or dictionary.

The key are special methods, or "dunder" methods. More information can be found
in the [data model docs](https://docs.python.org/3/reference/datamodel.html),
[special method
names](https://docs.python.org/3/reference/datamodel.html#special-method-names).

> A class can implement certain operations that are invoked by special syntax
> (such as arithmetic operations or subscripting and slicing) by defining
> methods with special names. This is Python’s approach to operator overloading,
> allowing classes to define their own behavior with respect to language
> operators. 

## Protocol: str and repr

* `__str__`
* `__repr__`

## Protocol: length

* `__len__`

## Protocol: item access

* `__getitem__`
* `__setitem__`
* `__delitem__`

```Python
class Sample:

    def __getitem__(self, key):
        return "42"

s = Sample()
print(s["hi"])
```

## Protocol: iteration

> Python supports a concept of iteration over containers. This is implemented
> using two distinct methods; these are used to allow user-defined classes to
> support iteration.

* `__iter__`
* `__next__`

The `StopIteration` exception serves as a sentinel value.


## Protocol: Equality

Beside a few other methods for object comparison, we can define:

* `__eq__` to customize equality checks

Example: A case insensitive strings class

```python
class Str(str):

    def __eq__(self, other):
        if not isinstance(other, str):
            raise TypeError
        return self.lower() == other.lower()

a = "Hello"
b = "hello"

print(a == b)
print(Str(a) == Str(b))
```

The
[functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering)
decorator will supply the rest of the comparison operators, if one or more
comparison ordering method is defined.


## Protocol: context manager

* resource setup and teardown
* typically used with files

Example for sqlite.

```python
class sqlitedb():
    """
    Simple cursor context manager for sqlite3 databases. Commits everything at exit.
        with sqlitedb('/tmp/test.db') as cursor:
            query = cursor.execute('SELECT * FROM items')
            result = query.fetchall()
    """
    def __init__(self, path, timeout=5.0, detect_types=0):
        self.path = path
        self.conn = None
        self.cursor = None
        self.timeout = timeout
        self.detect_types = detect_types

    def __enter__(self):
        self.conn = sqlite3.connect(self.path, timeout=self.timeout, detect_types=self.detect_types)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()
```



## Task: Context manager

Benchmarking context manager and decorator example.

1. Implement a context manager that can be used to track the execution time of a
   piece of code.

It could be used, e.g. like this:

```python
with Timer() as timer:
    result = some_function()
print(timer.elapsed_s) # prints out elapsed seconds
```

2. Implement a decorator called `@timed` which can be added to functions to
   measure their execution time. This decorator can use the context manager defined.

```python
@timed
def sum_numbers(n=10000):
    return sum(i for i in range(n))

sum_numbers(1_000)
sum_numbers(1_000_000)
sum_numbers(100_000_000)
```