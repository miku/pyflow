

def deco(n=0):
    def wrapped(f):
        def inner(*args, **kwargs):
            print("[deco] {} calling {}".format(n, f.__name__))
            result = f(*args, **kwargs)
            print("[deco] {} exited {}".format(n, f.__name__))
            return result
        return inner
    return wrapped



@deco(n=3)
def hello(name="world"):
    print("hello " + name)

hello()
