
class Gen:

    def __iter__(self):
        return self

    def __next__(self):
        return "42"


gen = Gen()
print(next(gen))
print(next(gen))
