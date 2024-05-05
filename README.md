# Advanced Python

> Concepts and techniques

Focus areas:

* [Clean Code](10-CleanCode.md)
* [Idiomatic](20-Idiomatic.md)
* [Safe](30-Safe.md)
* [Lifecycle](40-Lifecycle.md)
* [Performance](50-Performance.md)
* [Misc](60-Misc.md)


----

## Contents

* clean code
    * programming as a losers game
        * avoiding mistakes more important than methodology
    * software engineering (and greatest hits)
        * cohesion and coupling
            * [Difference Between Cohesion and Coupling](https://stackoverflow.com/questions/3085285/difference-between-cohesion-and-coupling) (461K views)
        * example from Ousterhout: "A Philosophy of Software Design"
        * the "Out of the tar pit" paper
            * a engineering dream
            * avoid mutable state and use pure functions
        * the "programming as theory building" paper
        * Parnas' module paper
        * the "worse is better" paper
        * software engineering's greatest hits
    * top-down and bottom-up approach
        * example: clickhouse, bottom-up
        * start with a gist, then expand
        * monolith and microservices
        * vertical and horizontal scaling
        * batch or realtime
    * small techniques
        * readme-driven development (TPW)
        * test-driven development
        * linting
        * is this code easy to delete?
        * is this code surprising?
        * eliminate a roadblock (MC)
        * find a way to iterate faster (AK)
        * make documentation look so good, you always want to read it (AR)
    * DDD
        * strategic and tactical designs
        * bounded context, ubiquitous language, context mapping
        * aggregate, domain events
    * design ideas
        * build code that composes, composition over inheritance
        * use the right concepts at the right time
* idiomatic python
    * python data model
        * overview
        * object identity
            * `is` vs `eq`
        * rendering (str, repr)
        * object creation
            * how objects are created in python
            * metaclasses
    * iteration
    * generators
    * decorators
    * well behaving objects
    * smart collections
    * mighty itertools
        * use case list for itertools
        * replace 50 lines with 1 line
    * when to use metaclasses
        * DSL
* design patterns
    * classic design patterns
        * object creation
        * composition
        * behaviour
    * pattern in python
* robustness
    * defensive programming
    * type hints
    * type checkers overview
    * everyday use of gradual typing
    * working with legacy code and type hints
* testing code with pytest
    * overview
    * fixtures
    * parameterized tests
    * marking tests
* development and deployment
    * general ideas
        * semantic versioning
        * private package repository
        * CI/CD gitlab example
    * minimal packaging
        * setup.py and pyproject
        * pip and pip-tools
        * uv as a modern replacement
    * PEP-441 based solutions
    * pyinstaller
    * containerized python
    * cookiecutter for unified structure
    * data-intensive applications
    * jupyter notebook reproducibilty
* robust data processing
    * data oriented programming
    * validation frameworks
    * named tuples and data classes
* performance
    * why python is slow
    * basic tricks
        * data structures (set, list)
        * insert and append
        * slots for slimmer objects
        * generators
    * GIL problems
    * multithreading
    * multiprocessing
    * async programming
    * array programming with numpy
    * dataframe evolution
    * cython
    * writing a c module
