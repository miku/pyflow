from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float # must be annotated
    lon: float
    reference: str = 'WGS84' # can have default values
    

a = Coordinate(lat=51.3397, lon=12.3731)
print(a)
print(a.__annotations__)

# Coordinate(lat=51.3397, lon=12.3731, reference='WGS84')
# {'lat': <class 'float'>, 'lon': <class 'float'>, 'reference': <class 'str'>}