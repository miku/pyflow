# first line: 7
@memory.cache
def f(x):
    print('Running f(%s)' % x)
    return x
