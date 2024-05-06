
import itertools

def fib():
    a, b = 1, 0
    while True:
        yield a + b
        a, b = b, a + b


for i in itertools.islice(fib(), 10):
    print(i)

def tail(n, iterable):
    "Return an iterator over the last n items."
    # tail(3, 'ABCDEFG') → E F G
    return iter(collections.deque(iterable, maxlen=n))

ratio = itertools.takewhile(lambda x, y: x / y > 0, itertools.pairwise(fib()))
print(list(ratio))