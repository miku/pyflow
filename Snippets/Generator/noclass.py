
def gen():
    i = 0
    while i < 3:
        i += 1
        yield i


for i in gen():
    print(i)