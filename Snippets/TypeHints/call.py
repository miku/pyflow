from typing import Callable

def f(g : Callable[..., int]) -> bool:
    return True


f(lambda x: x)
