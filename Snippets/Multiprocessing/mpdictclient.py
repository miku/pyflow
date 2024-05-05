# https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments

import multiprocessing as mp
from multiprocessing.managers import SyncManager

m = SyncManager(address=('127.0.0.1', 50000), authkey=b'abc')
m.connect()

d = m.dict()

def f(x):
    return x * x

def change(k, v):
    print("change!")
    d[k] = v

if __name__ == '__main__':

    pool = mp.Pool()
    args = zip("abcdefgh", range(10))
    print(list(args))
    pool.starmap(change, tuple(args))
    # pool.apply(change, (("a", 1), ("b", 2)))

    print(d)