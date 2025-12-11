import datetime
import time


def timer(func):
    def a():
        a = datetime.datetime.now()
        func()
        b = datetime.datetime.now()
        print(f"Function: {func.__name__} took {b - a} seconds")
    return a()

@timer
def delay():
    time.sleep(5)
