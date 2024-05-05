from typing import Sequence, TypeVar

S = TypeVar('S')
T = TypeVar('T')      # Declare type variable


def first(l: Sequence[T]) -> S:   # Generic function
    return l[0]


first([1, 2, 3])

# Snippets/TypeHints/other.py:8: error: Incompatible return value type (got "T", expected "S")
# Found 1 error in 1 file (checked 1 source file)
