from datetime import datetime
from functools import wraps
from time import sleep


def sleeper(seconds):
    def inner(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            print(f"Going to sleep for {seconds} seconds!")
            sleep(seconds)
            return fun(*args, **kwargs)
        return wrapper
    return inner


def execution_timer(fun):
    @wraps(fun)
    def inner(*args, **kwargs):
        start = datetime.now()
        result = fun(*args, **kwargs)
        stop = datetime.now()
        print(f"Execution time: {(stop-start).microseconds} microseconds")
        return result
    return inner


def execution_counter(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        wrapper.counter += 1
        print(f"\"{fun.__name__}\" has been called {wrapper.counter} times")
        return result
    wrapper.counter = 0
    return wrapper
