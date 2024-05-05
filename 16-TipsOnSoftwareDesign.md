# A few tips for Software Design

Inspired by:

* [Twelve quick tips for software design. PLoS Comput Biol 18(2): e1009809. https://doi.org/10.1371/journal.pcbi.1009809](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009809)


## Design after the fact

> Many designers explain the design of their software by recapitulating its
history [7,8]. This is sometimes called challenge and response: The only way to
understand why some- thing works the way it does is to understand the problems
that existed at the time it was written and the tools that were available then.

Relates to comments in code that describe the circumstance (and not what is written).

* approach: write first, design, refactor

## Design for people's cognitive capacity

* humans have a short term memory limit 
* How many details do I need to keep in my head as I am reading a particular
  piece of code?

## Design in coherent levels

* functions should be short, shallow and single purpose
* something that only takes up one slot in short term memory

You can ask: Between how many levels of detail do I need to jump while reading this code?

```python
def main():
    config = buildConfiguration(sys.argv)
    state = initializeState(config)
    while config.currentTime < config.haltTime:
        updateState(config, state)
    report(config, state)
```

The `while` condition could be taken "a level up", e.g. like:

```python
...
while stillEvolving(config, state):
   updateState(config, state)
   ...
```


## Design for Evolution

> More realistically, a change in one place should only require a small number
of changes in a few predictable places.

For example `stillEvolving` could be changed internally (to adapt), while client
code stays the same.

Two main ways:

* information hiding (interface, api and implementation)
* loose coupling (e.g. *command line*)

## Group related information together

What is easier to read?

```python
def enclose (x0, y0, z0, x1, y1, z1, nearness):
    ...
```

Or:

```python
def enclose (p0, p1, nearness):
    ...
```

## Design for delivery

* take care of the build process
* maybe a common way to build the project (e.g. Makefiles)
