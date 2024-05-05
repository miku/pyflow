
from collections import namedtuple

Point = namedtuple("Point", "x y z")


p1 = Point(1, 2, 3)
p2 = Point(x=1, z=3, y=2)

print(p1)
print(p2)
print(p1 == p2)
