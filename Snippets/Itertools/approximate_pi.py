
from itertools import islice

def madhava_leibniz() -> float:
    a, sign = 1, 1
    while True:
        yield sign * (1 / a)
        a = a + 2
        sign = -sign
    

for i in islice(madhava_leibniz(), 10):
    print(i)

approx = 4 * sum(islice(madhava_leibniz(), 1000)) # take first 1000 elements from stream
print(approx)

