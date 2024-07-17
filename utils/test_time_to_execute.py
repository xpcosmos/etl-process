import time
from typing import Callable

def time_measure(func:Callable) -> int:
    '''Decorator that reports the execution time.'''
    def measure(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Function: {func.__name__} took: {end-start:.3f}ms')
        return result
    return measure
