from datetime import datetime


def execution_timer(fun):
    def inner(*args, **kwargs):
        start = datetime.now()
        result = fun(*args, **kwargs)
        stop = datetime.now()
        print(f"Execution time: {(stop-start).microseconds} microseconds")
        return result
    return inner


def execution_counter(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        wrapper.counter += 1
        print(f"\"{fun.__name__}\" has been called {wrapper.counter} times")
        return result
    wrapper.counter = 0
    return wrapper
