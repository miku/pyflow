# immutable object with a builder and namedtuple

import collections

Location = collections.namedtuple("Location", "x y z")


class SiteBuilder:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def build(self):
        return Site(x=self.x, y=self.y, z=self.z)


class Site(Location):
    __slots__ = ()

    def __str__(self):
        return f"<Site x={self.x}, y={self.y}, z={self.z}>"


builder = SiteBuilder(1, 2)
obj1 = builder.build()
builder.x = 100
obj2 = builder.build()
builder.y = 200
obj3 = builder.build()

print(obj1)
print(obj2)
print(obj3)

# obj3.x = 500
# Traceback (most recent call last):
#   File "/home/tir/code/miku/pyflow/chapters/Misc/immutable_with_namedtuple.py", line 35, in <module>
#     obj3.x = 500
# AttributeError: can't set attribute
