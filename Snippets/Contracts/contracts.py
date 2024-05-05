"""
Example of a design-by-contract library in Python, https://icontract.readthedocs.io.
"""

import icontract


@icontract.require(lambda x: x > 3)
def some_func(x: int, y: int = 5) -> None:
    pass


# some_func(x=1)

# icontract.errors.ViolationError: File contracts.py, line 7 in <module>:
# x > 3:
# x was 1
# y was 5


class B:
    def __init__(self) -> None:
        self.x = 7

    def y(self) -> int:
        return 2

    def __repr__(self) -> str:
        return "an instance of B"


class A:
    def __init__(self) -> None:
        self.b = B()

    def __repr__(self) -> str:
        return "an instance of A"


SOME_GLOBAL_VAR = 13


@icontract.require(lambda a: a.b.x + a.b.y() > SOME_GLOBAL_VAR)
def some_func(a: A) -> None:
    pass

an_a = A()
some_func(an_a)

# Traceback (most recent call last):
#   File "contracts.py", line 48, in <module>
#     some_func(an_a)
#   File "/home/tir/.virtualenvs/cleancodepython/lib/python3.8/site-packages/icontract/_checkers.py", line 631, in wrapper
#     raise violation_error
# icontract.errors.ViolationError: File contracts.py, line 43 in <module>:
# a.b.x + a.b.y() > SOME_GLOBAL_VAR:
# SOME_GLOBAL_VAR was 13
# a was an instance of A
# a.b was an instance of B
# a.b.x was 7
# a.b.y() was 2

