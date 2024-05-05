from dataclasses import dataclass

@dataclass()
class Point:
     x: int # if no default given, the field will be required
     y: int 


p = Point(2, 3)
# q = Point(2) # TypeError

print(p)