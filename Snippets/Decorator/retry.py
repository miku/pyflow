import time

def retry(count=3, sleep=0):
    """
    @retry():
    def some_func():
        pass
    @retry(count=2, sleep=1):
    def some_func():
        pass
    """

    def __decorator(func):
        def __retry_func(*args, **kwargs):
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    time.sleep(sleep)
                    last_exc = exc
            raise last_exc

        return __retry_func

    return __decorator

