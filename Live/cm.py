import datetime
import time


class Timer:
    # started_at: datetime.datetime
    # elapsed_seconds: int

    def __enter__(self):
        self.started_at = datetime.datetime.now()
        return self

    def __exit__(self, exc_class, exc, traceback):
        self.elapsed_seconds = (datetime.datetime.now() - self.started_at).seconds


# with Timer() as timer:
#     print("inside context manager")
#     time.sleep(3)
# print(f"elapsed: {timer.elapsed_seconds}")


def timed(f):
    def inner(*args, **kwargs):
        with Timer() as timer:
            result = f(*args, **kwargs)
        print(f"{f.__name__} took {timer.elapsed_seconds}")
        return result
    return inner 

# add = timed(add)

@timed
def add(a, b):
    time.sleep(2)
    return a + b

print(add(1, 2))