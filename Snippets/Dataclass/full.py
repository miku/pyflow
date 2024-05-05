from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=False, frozen=False)
class Point:
     x: int
     y: int


p = Point(2, 3)

print(p)