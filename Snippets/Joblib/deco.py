from joblib import Memory

cachedir = '.cachedir'
memory = Memory(cachedir, verbose=0)


@memory.cache
def f(x):
    print('Running f(%s)' % x)
    return x



f(10)
f(10)
f(11)
f(11)