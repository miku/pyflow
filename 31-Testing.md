## The pytest project

* python has [unittest](https://docs.python.org/3/library/unittest.html) is
  standard library, classic framework (inspired by JUnit)
* setUp, tearDown, assertTrue, assertEquals, assertRaises, ...

The basic notions are similar:

* fixture
* test case
* test suite
* test runner

* one goal of pytest was to be a bit more pythonic (with unittest coming fro
JUnit)
* helpful messages

### Basics

* pytest detects tests by name prefix, e.g. `test_*` functions and methods
* grouping in a class possible
* only a single `assert`

Calling pytest with filename, directory or via name filter `-k` to select
specific files.

```
$ pytest test_fixture.py
$ pytest -k fix
```

### Marks

* setting metadata on functions
* a list of builtin marks can be found here: [marks](https://docs.pytest.org/en/stable/reference.html#marks-ref)

For example, you can mark a test function with
[skipif](https://docs.pytest.org/en/stable/reference.html#pytest-mark-skipif) to
skip under certain conditions; or
[xfail](https://docs.pytest.org/en/stable/reference.html#pytest-mark-xfail) to
expect a failed test.

### Fixtures

* pytest approach to fixtures is interesting, as it is mostly name based

If we run this, we do not get any output.

```python
def test_hello(tmpdir):
    print(tmpdir)
```

The test would pass, but not print anything on this successful test.

```
platform linux -- Python 3.7.8, pytest-6.1.1, py-1.9.0, pluggy-0.13.1
rootdir: /home/tir/code/miku/cleancodepython/Snippets/TestingBasic
collected 1 item                                             

test_fixture.py .                                                            [100%]
```

We need to pass `-s` shortcut to see the output, as pytest offers various capture method.

```
  --capture=method      per-test capturing method: one of fd|sys|no|tee-sys.
  -s                    shortcut for --capture=no.
```

Default:

> During test execution any output sent to stdout and stderr is captured. If a
> test or a setup method fails its according captured output will usually be
> shown along with the failure traceback.

The output can be captured on a filesystem (fd 0 and 1) level (e.g. when calling
external commands) or on `sys.write` level. The `tee-sys` captures and passes
through output, like the tee (T) command.

* Example: [Snippets/Testing](Snippets/Testing), `test_ls.py`

There are more builtin fixtures:

* [https://docs.pytest.org/en/stable/builtin.html](https://docs.pytest.org/en/stable/builtin.html)

Examples are: caching values, capturing logging messages, recording warnings

### Fixture: monkeypatch

> monkeypatch can be used to patch functions dependent on the user to always
> return a specific value.

* Example: [Snippets/Testing](Snippets/Testing), `test_ssh.py`

### Custom fixture

Fixtures can provide various test dependencies. They are a form of dependency
injection.

You can include these in your testfiles or in `conftest.py` to be shared by multiple tests.

A fixture can be valid in different scopes:

> Fixtures requiring network access depend on connectivity and are usually
> time-expensive to create. Extending the previous example, we can add a
> scope="module" parameter to the @pytest.fixture invocation to cause the
> decorated smtp_connection fixture function to only be invoked once per test
> module (the default is to invoke once per test function). 

> Possible values for scope are: function, class, module, package or session.

Initialization goes from session to function.

A fixture can handle both setup and teardown, when using `yield` at the point
where execution should continue in the test.

Examples:

* `test_fixture_custom.py`
* `test_fixture_autouse.py`
* `test_fixture_yield.py`

### Other plugins

* common data directory for test files:
  [pytest-datadir](https://pypi.org/project/pytest-datadir/) or
  [pytest-datafiles](https://pypi.org/project/pytest-datafiles/)


## Table Driven Tests

Not a new idea, but popularized a bit more by Go:

* [https://github.com/golang/go/wiki/TableDrivenTests](https://github.com/golang/go/wiki/TableDrivenTests)

* boil down cases to rows in a table
* can be also pushed out (e.g. to CSV file or similar)

## Code coverage

Coverage measures the ratio of tested lines of code and lines of code. 100%
coverage does not mean bug free.

Automated tool:

* [https://coverage.readthedocs.io/en/coverage-5.3/](https://coverage.readthedocs.io/en/coverage-5.3/)

You can run it standalone:

```
$ coverage run -m pytest -v
```

This will generate an sqlite3 database, be default `.coverage`. Generate a report:

```
$ coverage report -i gluish/*
Name                  Stmts   Miss  Cover
-----------------------------------------
gluish/__init__.py        8      0   100%
gluish/common.py        117     59    50%
gluish/format.py         70     30    57%
gluish/intervals.py      27     15    44%
gluish/parameter.py       5      0   100%
gluish/task.py           77     55    29%
gluish/utils.py          54     30    44%
-----------------------------------------
TOTAL                   358    189    47%
```

Or install a pytest plugin for coverage.

```
$ pip install pytest-cov
```

Run alongside tests:

```
$ pytest --cov=gluish -v gluish/*
```

Various outputs are available, e.g. HTML.

## Other testing helpers

requests is a popular HTTP library,
[responses](https://github.com/getsentry/responses) is a great addition to test
HTTP interactions.

```python
@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps

def test_api(mocked_responses):
    mocked_responses.add(
        responses.GET, 'http://twitter.com/api/1/foobar',
        body='{}', status=200,
        content_type='application/json')
    resp = requests.get('http://twitter.com/api/1/foobar')
    assert resp.status_code == 200
```

## Other Plugins

* [1402](https://pypi.org/search/?q=name%3Apytest&o=-created) projects with "pytest" in their name (not all plugins, presumably)

A few interesting ones may be:

* [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) - for web application testing
* [pytest-clarity](https://github.com/darrenburns/pytest-clarity) - for improved diffs

## Extra Tools

There are different testing helpers for various circumstances.

Mutation testing:

> [https://github.com/mutpy/mutpy](https://github.com/mutpy/mutpy)

Tries to modify code slightly.

> Mutation testing (or Mutation analysis or Program mutation) evaluates the
> quality of software tests. Mutation testing involves modifying a program's
> source code or byte code in small ways. A test suite that does not detect and
> reject the mutated code is considered defective.

* limited [pytest support](https://github.com/mutpy/mutpy/issues/17) (but test runner seems ok)

Example: [Snippets/MutPy]

