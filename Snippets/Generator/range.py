
class Range:

    def __init__(self, start=0, stop=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.i = start

    def __iter__(self):
        return self

    def __next__(self):
        v = self.i
        self.i += self.step
        if self.i > self.stop:
            raise StopIteration
        return v


    
def rangeg(start=0, stop=0, step=1):
    i = start
    while i < stop:
        yield i
        i += step



# for i in rangeg(0, 10, 2):
#    print(i)
    

for i in Range(0, 10, 2):
    print(i)
