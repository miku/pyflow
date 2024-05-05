# Design Patterns

A look into design patterns and their applications Python.

## Favor object composition over class inheritance

* you can extend classes along multiple "axes", which leads to "class proliferation"
* standard library "logging" is an example of "composition over inheritance"

### Logging

With inheritance only, you could wind up with:

* Logger
* StdoutLogger
* StderrLogger
* FilteredStdoutLogger
* ...

Various ways to adapt:

* **Adaptor** pattern, using a conventional interface, e.g. the "write" method and
  wrap all output modalities in a new class supplying this function, adapting to
  the needs of the logger.
* **Bridge**, similar to Adaptor, but using a custom abstraction, e.g. a message
  that works slightly higher in the hierarchy (e.g. passing a message, versus
  "write")

> "Adapter makes things work after they're designed; Bridge makes them work
> before they are. [GoF, p219]"

* **Decorator** pattern

If a filter wraps a logger with the same method name, e.g. `log`, we can stack
them.

```python

class Filter:
    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger

    def log(self, message):
        if pattern in message:
            self.logger.log(message)

log1 = SomeLogger("app.log")
log2 = Filter("debug", log1)
log3 = Filter("todo", log2)
...
```

The way the standard library implements logging is by separating loggers, formatters, handlers.

> Handler objects are responsible for dispatching the appropriate log messages
> (based on the log messages’ severity) to the handler’s specified destination. 

* streams, files

Actually, more the
[docs](https://docs.python.org/3/howto/logging.html#useful-handlers) list more
than 10 implementations, like `TimeRotatingFileHandler` and `HTTPHandler`.

> Formatter objects configure the final order, structure, and contents of the
> log message. Unlike the base logging.Handler class, application code may
> instantiate formatter classes, although you could likely subclass the
> formatter if your application needs special behavior. 

Putting these things together:

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

## MVC

* model view controller, separation of concerns

Often used in frameworks with UI elements.

* web frameworks
* GUI frameworks, although Tkinter seems to have a more tighter coupling

In web framworks the separation goes along:

* database abstraction and queries (M)
* mostly logic-less HTML templates (V)
* handing of the request-response cycle (C)

In desktop toolkits, you will have some **Observer** pattern implemented.

For example in a classic (Java) example, the tabular data model (`TableModel`) can
inform other components about change via `addTableModelListener`, propagating events.

A test for true MVC design:

> Is the program functional even without the view? Or the controller?

## Global objects

* similar to singletons

Often used for constants, defined on module level and exported.

Special cases, e.g. *dunder* constants, like `__version__`.

A few builtin dunder names:

* `__file__` (the current file)
* `__name__` (the name of the module, e.g. `__main__` when invoked from the command line)

## Abstract Factory

Factories are classes that build objects. Not really needed in Python.

> But Python has the concept of callables, which typically allow to pass in the
> class itself.

Python has first class functions, which are callable. Methods are callable, and
classes are, too, if they implement `__call__`.

There are alternatives:

* a simple function
* a method on a class
* a generator with some state

```python
class Switch:
    def __init__(self):
        self.on = False
    def __call__(self):
        print("switch is {}".format("on" if self.on else "off"))
        self.on = bool(1 - self.on)


switch = Switch()
switch()
switch()
```

For specifying required functionality, create an abstract class by returning
`NotImplementedError` on the methods that subclasses need to provide. 

Another Take on Abstract Factory.

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


## Singleton pattern

Examples: [Snippets/Singleton](Snippets/Singleton)

* overwriting `__new__`
* not that pronounced either, use global object instead

## Iterator pattern

There is concept of an iterator in Python (in
[iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)),
[iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator).

* `iter` has a dual role; it turns a sequence into an iterator or allows to use
  a callable to create a sequence

Example application, reading a file in blocks:

```python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)
```

> Return a new *partial* object which when called will behave like func called
> with the positional arguments args and keyword arguments keywords.


## Facade

* providing a simplified interface while delegating work to one or more other classes


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

There is a possible, but less common use case to let a mutable builder object build an immutable object.


## Decorator Pattern

* is an adapter, that does not change the interface of the wrapped object
* can help with separation of concerns

Examples:

* caching/memoization in joblib
* extra setup or cleanup around a method

Because Python supports introspection, wrapped object look different from the original. 


## Wrap Up

Design patterns exists, but some of the original patterns are less prevalent as
Python constructs exist to (partially) address the problems.

