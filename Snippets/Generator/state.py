
class Gen:

    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < 4:
            return self.i
        else:
            raise StopIteration

gen = Gen()
for i in gen:
    print(i)