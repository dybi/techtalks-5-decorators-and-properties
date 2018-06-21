from datetime import datetime


def execution_timer(fun):
    def inner(*args, **kwargs):
        start = datetime.now()
        fun(*args, **kwargs)
        stop = datetime.now()
        print(f"Execution time: {(stop-start).microseconds} microseconds")
    return inner
