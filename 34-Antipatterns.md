# A few more Python Patterns and Anti-Patterns

Everything that pylint (or other linter) can be an opportunity to improve code.

* [http://pylint-messages.wikidot.com/all-codes](http://pylint-messages.wikidot.com/all-codes)

## Pairwise iteration with zip

* using builtin [zip](https://docs.python.org/3.3/library/functions.html)

```
vs = [1, 2, 3]
letters = ["A", "B", "C"]

for index in range(len(vs)):
    print(vs[index], letters[index])
```

With `zip` we can write the loop as a parallel iteration:

```
vs = [1, 2, 3]
letters = ["A", "B", "C"]

for v, letter in zip(vs, letters):
    print(v, letter)
```

## Test Object Identity with `is`

We have both `==` and `is` is Python.

* `is` compares reference
* `==` compares values (can be any custom procedure)

No need to write:

```
if x == True:
    ...
```

Better:

```
if x is True:
    ...
```

Or just:

```
if x:
    ...
```

It can improve readability when dealing with collections and we want to check
for the existence, we pull in `len` - to be explicit.

```python
vs = []
if vs:
    ....
```

Alternative:

```python
vs = []
...

if len(vs) == 0:
    ...
```

## Using `type` to compare types

* use `isinstance` instead, as it will cater for inheritance


## Using index variables in for loops

Use the builtin enumerate:

```python
seq = list('abc')
for i, v in enumerate(seq):
    print(i, v)
```

## Use tuple unpacking

```python
def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a
```

Tuple unpacking allows for:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

## Star-imports

In general, you should not need star imports:

```python
from module import *
```

What is exported can be controlled with the `__all__` special variable.


## Plain open files

We can open and close files manually:

```python
f = open("file.txt")
f.close()
```


But context managers are encouraged:

```python
with open("file.txt") as f:
    pass
```

## Varied return types

Rare, but it this is used it can be confusing - even though dynamic typing allows for any return type.

```python
def f(x=0):
    if x > 0:
        return x
    else:
        return False
```

