import functools
from timeit import default_timer

class Timer:
    """
    A timer as a context manager.
    """
    def __init__(self):
        """
        Indicate runtimes with colors, green < 10s, yellow < 60s.
        """
        # measures wall clock time, not CPU time!
        # On Unix systems, it corresponds to time.time
        # On Windows systems, it corresponds to time.clock
        self.timer = default_timer

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = self.timer()
        self.elapsed_s = self.end - self.start
        self.elapsed_ms = self.elapsed_s * 1000


def timed(method):
    """
    A @timed decorator.
    """
    @functools.wraps(method)
    def _timed(*args, **kwargs):
        """
        Benchmark decorator.
        """
        with Timer() as timer:
            result = method(*args, **kwargs)
        fun = method.__name__
        msg = '[%s] %0.5f' % (fun, timer.elapsed_s)
        print(msg)
        return result

    return _timed


@timed
def sum_numbers(n=10000):
    return sum(i for i in range(n))

sum_numbers(1_000)
sum_numbers(1_000_000)
sum_numbers(100_000_000)