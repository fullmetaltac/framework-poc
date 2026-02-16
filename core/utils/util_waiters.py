from inspect import stack
from time import sleep, time
from typing import Any, Callable

from core.utils.util_exceptions import MaxRetriesExceeded


def _get_caller(func):
    _stack = stack()
    for i, f in enumerate(_stack):
        if f.function == func.__name__:
            return _stack[i + 2].function + " → " + _stack[i + 1].function
    return _stack[-1].function + " → " + _stack[-2].function


def wait_for(condition: Callable[..., Any], timeout=10, interval=0.5):
    start_time = time()
    while True:
        if condition():
            return True
        if time() - start_time > timeout:
            raise TimeoutError(f"{_get_caller(wait_for)} was not met after {timeout} seconds")
        sleep(interval)


def xtry(func: Callable[[], Any], condition: Callable[..., Any], count=3, interval=0.5):  # pylint: disable=R1710
    for i in range(count):
        result = func()
        if condition(result) if condition.__code__.co_argcount else condition():
            return result
        if i == count - 1:
            raise MaxRetriesExceeded(f"{_get_caller(xtry)} execution failed after {count} attempts")
        sleep(interval)
