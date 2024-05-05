
from typing import List


# variable annotation
a : int = 2 
b : float = 1.0

# type aliases
Vector = List[float]

# function annotation
def add(u, v : Vector):
    return u + v

print(a, b)
print(add(1.0, 2.0))