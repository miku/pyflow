# Pyproject

* attempt to improve on `setup.py` based workflows
* declarative TOML configuration
* more on [pypa pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

Classic projects are still use `setup.py`, e.g.

* Pandas: [setup.py](https://github.com/pandas-dev/pandas/blob/main/setup.py), [pyproject.toml](https://github.com/pandas-dev/pandas/blob/main/pyproject.toml)
* Luigi: [setup.py](https://github.com/spotify/luigi/blob/master/setup.py)
* PyMARC: [setup.py](https://gitlab.com/pymarc/pymarc/-/blob/main/setup.py?ref_type=heads)
* boto3: [setup.py](https://github.com/boto/boto3/blob/develop/setup.py), [pyproject.toml](https://github.com/boto/boto3/blob/develop/pyproject.toml) (stub)

The classic workflow mostly worked with an additional library called [setuptools]() and invocations like:

```
$ python setup.py sdist # bdist, ...
```

Since [PEP-518](https://peps.python.org/pep-0518/) and other [packaging
PEPs](https://peps.python.org/topic/packaging/) we are seeing a new landscape of
projects.


## Virtual envs

```
$ alias mkvenv
alias mkvenv='python -m venv .venv && source .venv/bin/activate' # then deactivate
```


## Just a few tools from the packaging universe

* pyenv (NA)

> pyenv lets you easily switch between multiple versions of Python. It's simple,
> unobtrusive, and follows the UNIX tradition of single-purpose tools that do
> one thing well.

* pip (360M)

> pip supports installing from PyPI, version control, local projects, and
> directly from distribution files.

Can install directly from a file:

```
$ python -m pip install -r requirements.txt
```

* pipx (7M)

> pipx is a tool to help you install and run end-user applications written in
> Python. It's roughly similar to macOS's brew, JavaScript's npx, and Linux's
> apt

Example:

```
$ pipx install PACKAGE
```

This automatically creates a virtual environment, installs the package, and adds
the package's associated applications (entry points) to a location on your PATH.
For example, pipx install pycowsay makes the pycowsay command available
globally, but sandboxes the pycowsay package in its own virtual environment.
pipx never needs to run as sudo to do this.

Temporary envs are supported via `run`, e.g.

```
$ pipx run pycowsay moo
```

* pip-tools (11M)

> The pip-compile command lets you compile a requirements.txt file from your
> dependencies, specified in either pyproject.toml, setup.cfg, setup.py, or
> requirements.in.

This package comes with `pip-compile` (to build a requirements.txt) and
`pip-sync` (to sync deps and a venv).

* pipenv (10M)

> Pipenv automatically creates and manages a virtualenv for your projects, as
> well as adds/removes packages from your Pipfile as you install/uninstall
> packages. It also generates a project Pipfile.lock, which is used to produce
> deterministic builds.

* virtualenv (117M)

> virtualenv is a tool to create isolated Python environments. **Since Python 3.3,
> a subset of it has been integrated into the standard library under the venv
> module.** The venv module does not offer all features of this library, to name
> just a few more prominent:

* virtualenvwrapper (160K)

> virtualenvwrapper is a set of extensions to Ian Bicking’s virtualenv tool. The
> extensions include wrappers for creating and deleting virtual environments and
> otherwise managing your development workflow, making it easier to work on more
> than one project at a time without introducing conflicts in their
> dependencies.

* poetry (33M), [#3](https://github.com/python-poetry/roadmap/issues/3), [#3332](https://github.com/python-poetry/poetry/issues/3332)

> For example, I've noticed that poetry init generates a pretty similar
> pyproject.toml, but puts the metadata in a poetry-specific section.

* setuptools (391M)

> The first step towards sharing a Python library or program is to build a
> distribution package. [...] Also note that setuptools is what is known in the
> community as build backend, user facing interfaces are provided by tools such
> as pip and build. 

* hatch (1.6M)

> **Hatchling**, the **build** backend sister project, has many benefits compared to
> setuptools.

When not to use: "If building extension modules is required then it is
recommended that you continue using setuptools, or even other backends that
specialize in interfacing with compilers."

Note: hatch overlaps with pyenv, tox, setuptools; however there are gaps
compared to all these tools.


* flit (450K)

> Flit is a simple way to put Python packages and modules on PyPI. It tries to
> require less thought about packaging and help you avoid common mistakes.

The `flit` project uses `pyproject.toml` and has an easy publishing workflow, via `flit publish`.

> Specifically, the easy things are pure Python packages with no build steps
> (neither compiling C code, nor bundling Javascript, etc.). The vast majority
> of packages on PyPI are like this: plain Python code, with maybe some static
> data files like icons included.

* tox (14M)

> tox aims to automate and standardize testing in Python. It is part of a larger
> vision of easing the packaging, testing and release process of Python software 

* nox (2M)

> nox is a command-line tool that automates testing in multiple Python
> environments, similar to tox. Unlike tox, Nox uses a standard Python file for
> configuration. [...] Nox is lucky to have over 3,000 wonderful projects that
> use it and provide feedback and contributions (incl Jupyter, pip, pipx, google-cloud-python, ...)


* enscons (70K)

> Enscons is a Python packaging tool based on SCons. It builds pip-compatible
> source distributions and wheels without using distutils or setuptools,
> including distributions with C extensions. [...] Enscons implents a PEP 518
> build backend, and a setup.py shim that can be used for pip install -e .

* twine (6M)

> Twine is a utility for publishing Python packages to PyPI and other
> repositories. It provides build system independent uploads of source and
> binary distribution artifacts for both new and existing projects.

PYPA - the python packaging authority maintains a list of recommended tools:

* [https://packaging.python.org/en/latest/guides/tool-recommendations/](https://packaging.python.org/en/latest/guides/tool-recommendations/)

## Build frontend

* pip
* build

Build backends:

* different functionality, e.g. support for extensions

Example pyproject based project.

The `setup.py` based workflow is deprecated.

> Do not use python setup.py sdist and python setup.py bdist_wheel for this
> task. All direct invocations of setup.py are deprecated.


```
$ pip install build
$ python -m build # --sdist --wheel
```

Note: Discussions about `pyproject.toml` are still ongoing, see: [https://discuss.python.org/t/projects-that-arent-meant-to-generate-a-wheel-and-pyproject-toml/29684/21?page=2](https://discuss.python.org/t/projects-that-arent-meant-to-generate-a-wheel-and-pyproject-toml/29684/21?page=2)

## Distributions

* source - source and metadata
* binary - precompiled binaries (if any), the current format is called wheel ("whl" files)

A source distribution contains the source files only, may need to be compiled on
the target machine (if if contains a C extension).

A binary distribution contains precompiled code.

A wheel is a zip file, following a naming convention:

```
{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl
```

Example:

```
cryptography-2.9.2-cp35-abi3-macosx_10_9_x86_64.whl
```

Some (pure python) wheels work across platforms, hence they look a bit different
(ABI "none", playform "any").

```
chardet-3.0.4-py2.py3-none-any.whl
```

Example wheels from [Pandas](https://pypi.org/project/pandas/#files).

To examine a download locally, you can run `pip download`, best in a temporary folder. 

```
python -m pip download --only-binary :all: --dest . --no-cache numpy
```

On my machine, this results in a file:

```
./numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

This file contains shared library for "linux", cf.

```
$ unzip -l numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl | grep '[.]so'
    97008  2024-02-05 22:00   numpy/fft/_pocketfft_internal.cpython-312-x86_64-linux-gnu.so
    29849  2024-02-05 22:00   numpy/linalg/lapack_lite.cpython-312-x86_64-linux-gnu.so
   216793  2024-02-05 22:00   numpy/linalg/_umath_linalg.cpython-312-x86_64-linux-gnu.so
   125040  2024-02-05 22:00   numpy/random/_pcg64.cpython-312-x86_64-linux-gnu.so
   348704  2024-02-05 22:00   numpy/random/_bounded_integers.cpython-312-x86_64-linux-gnu.so
   749040  2024-02-05 22:00   numpy/random/mtrand.cpython-312-x86_64-linux-gnu.so
   119488  2024-02-05 22:00   numpy/random/_mt19937.cpython-312-x86_64-linux-gnu.so
   946872  2024-02-05 22:00   numpy/random/_generator.cpython-312-x86_64-linux-gnu.so
   258888  2024-02-05 22:00   numpy/random/_common.cpython-312-x86_64-linux-gnu.so
    76224  2024-02-05 22:00   numpy/random/_sfc64.cpython-312-x86_64-linux-gnu.so
   106712  2024-02-05 22:00   numpy/random/_philox.cpython-312-x86_64-linux-gnu.so
   234016  2024-02-05 22:00   numpy/random/bit_generator.cpython-312-x86_64-linux-gnu.so
  7463681  2024-02-05 22:00   numpy/core/_multiarray_umath.cpython-312-x86_64-linux-gnu.so
   175912  2024-02-05 22:00   numpy/core/_multiarray_tests.cpython-312-x86_64-linux-gnu.so
    59776  2024-02-05 22:00   numpy/core/_rational_tests.cpython-312-x86_64-linux-gnu.so
    42272  2024-02-05 22:00   numpy/core/_umath_tests.cpython-312-x86_64-linux-gnu.so
    16856  2024-02-05 22:00   numpy/core/_operand_flag_tests.cpython-312-x86_64-linux-gnu.so
    16960  2024-02-05 22:00   numpy/core/_struct_ufunc_tests.cpython-312-x86_64-linux-gnu.so
  3535232  2024-02-05 22:00   numpy/core/_simd.cpython-312-x86_64-linux-gnu.so
 35123345  2024-02-05 22:00   numpy.libs/libopenblas64_p-r0-0cf96a72.3.23.dev.so
   247609  2024-02-05 22:00   numpy.libs/libquadmath-96973f99.so.0.0.0
  2686065  2024-02-05 22:00   numpy.libs/libgfortran-040039e1.so.5.0.0
```

Different types of wheels:

* universal (py2/3)
* pure-python
* platform


## Back to the build

```shell
$ python -m build
$ twine upload -r testpypi dist/* # twine upload dist/*
```

* [https://twine.readthedocs.io/en/stable/#using-twine](https://twine.readthedocs.io/en/stable/#using-twine)

If you configure twine in your CI - e.g. with [environment
variables](https://twine.readthedocs.io/en/stable/#environment-variables), you
can upload your package to an artifact server.

## Local testing

Editable installs.

```
$ python -m pip install -e .
```


## Upload to testpypi via twine

```
$ twine upload -r testpypi dist/*
```

## Use your package

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install --index-url https://test.pypi.org/simple/ wettr
$ wettr-cli
```

You may run into:

* [Pip install from pypi works, but from testpypi fails (cannot find requirements)](https://stackoverflow.com/questions/34514703/pip-install-from-pypi-works-but-from-testpypi-fails-cannot-find-requirements)

```
$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple wettr
$ wettr-cli
```

## Configuring ruff in the pyproject.toml

* [https://docs.astral.sh/ruff/configuration/](https://docs.astral.sh/ruff/configuration/)

## Adding type-hints in pyproject.toml

```
$ mypy wettr
wettr/cache.py:5: error: Library stubs not installed for "requests"  [import-untyped]
wettr/cache.py:5: note: Hint: "python3 -m pip install types-requests"
wettr/cache.py:5: note: (or run "mypy --install-types" to install all missing stub packages)
wettr/cache.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 3 source files)
```

Install stubs for requests via `mypy --install-types` or [ignore imports](https://mypy.readthedocs.io/en/stable/running_mypy.html), via

```
ignore_missing_imports = True
```

## Adding tests

* tests can live in `tests/` subdir or alongside code
* pyproject does not have support for dev-dependencies yet, cf. [https://discuss.python.org/t/development-dependencies-in-pyproject-toml/26149/4](https://discuss.python.org/t/development-dependencies-in-pyproject-toml/26149/4), also: [PEP0735](https://peps.python.org/pep-0735/)


There is some workaround: [https://hynek.me/til/pip-tools-and-pyproject-toml/](https://hynek.me/til/pip-tools-and-pyproject-toml/)

```
$ pytest
```

## Pinned dependencies

> Python libraries should not pin dependencies. _Applications_ can pin
> dependencies, including all recursive dependencies of their libraries. There
> are tools like Pipenv and Poetry to make that easy.

Via pip-tools.


## Experimental packaging

* [https://stackoverflow.com/questions/72597315/how-to-build-pex-or-shiv-package-from-pyproject-compliant-project](https://stackoverflow.com/questions/72597315/how-to-build-pex-or-shiv-package-from-pyproject-compliant-project)

> shiv is a command line utility for building fully self contained Python
> zipapps as outlined in PEP 441, but with all their dependencies included.

```
$ make wettr.pyz
```

## Shipping a pyinstaller based package

> PyInstaller reads a Python script written by you. It analyzes your code to
> discover every other module and library your script needs in order to execute.
> Then it collects copies of all those files – including the active Python
> interpreter! – and puts them with your script in a single folder, or
> optionally in a single executable file.

```
$ pip install pyinstaller
```

Example:

```
$ make exe
```