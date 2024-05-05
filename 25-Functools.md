# Functools

> The functools module is for higher-order functions: functions that act on or return other functions. 

Example: caches.

```python
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
```

Also: `lru_cache`

Functools contains a helper for decorators as well, namely
[functools.wraps](https://docs.python.org/3/library/functools.html#functools.wraps).