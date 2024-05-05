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

## Functools Helper

* we can wrap the inner function (with a decorator) to keep name and docstring

```python
from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()

print(example.__name__)
print(example.__doc__)
```
