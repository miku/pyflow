
def my_enumerate(seq, start=0):
    i = start
    for v in seq:
        yield (i, v)
        i += 1 


for i, v in my_enumerate(["a", "b", "c"], start=10):
    print(i, v)