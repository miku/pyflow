## Generators

> A function which returns a generator iterator. It looks like a normal function
> except that it contains yield expressions for producing a series of values
> usable in a for-loop or that can be retrieved one at a time with the next()
> function.

> Each yield temporarily suspends processing, remembering the location execution
> state (including local variables and pending try-statements). When the
> generator iterator resumes, it picks up where it left off (in contrast to
> functions which start fresh on every invocation).

Analogously to list comprehensions, you have generator expressions.

You can implement generators by implementing a class that implements two functions:

* `__iter__`
* `__next__`

Example: [Snippets/Generator](Snippets/Generator)

```python
class Gen:

    def __iter__(self):
        return self

    def __next__(self):
        return "42"


gen = Gen()
print(next(gen))
print(next(gen))

```

It gets more interesting, when you have state that is kept between invocations.

```python
class Gen:

    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < 4:
            return self.i
        else:
            raise StopIteration

gen = Gen()
for i in gen:
    print(i)
```

Finally, the `yield` keyword allows to write a generator without a class.

```python
def gen():
    i = 0
    while i < 3:
        i += 1
        yield i


for i in gen():
    print(i)
```

Differences:

* less code
* we do not need to implement the protocol ourselves

> As a short exercise: Try to implement a generator that behaves like the builtin
`enumerate` - used for indexed iteration.

### Generator use cases

* os.walk
* processing pipelines

A number example:

```python
numbers = (i for i in range(1, 10))
squared = (i*i for i in numbers)
filtered = (i for i in squared if i % 7 == 0)

for v in filtered:
    print(v)
```

Example image processing pipeline:

* iterates over a list of files
* resizes the images
* pads each image with a border

```python
imgs = (imageio.imread(f) for f in filenames)
imgs = (resize_image(img, width=width) for img in imgs)
imgs = (pad_image(img, border=border, bordercolor=bordercolor) for img in imgs)
```

After these three lines, nothing will happen because generators are lazy and
nothing has been evaluated so far.

You can imaging doing something with a single image and then write it out.

Advantages:

* pipeline is extendable
* memory efficient
* pythonic (other languages do need more workarounds)

## Generators and itertools

* generators and itertools go great together
* [Snippets/Itertools](Snippets/Itertools)


## Task

Write a generator that mimics the builtin range without using `range`.

* use a class based approach and
* a generator function approach

Example usage would be like:

```python
for i in Range(0, 10, 2):
    print(i)

# 0
# 2
# 4
# 6
# 8
```

