from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
     x: int
     y: int


p = Point(2, 3)

print(p)

# p.x = 4 # dataclasses.FrozenInstanceError: cannot assign to field 'x'