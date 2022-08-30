
# for more information see this link : 
# https://www.geeksforgeeks.org/timing-functions-with-decorators-python/


# an example for writing a decorator --> general form
def my_decorator(func):
    def wrapper_function(*args, **kwargs):
        print("*"*10)
        func(*args,  **kwargs)
        print("*"*10)
    return wrapper_function


# time consuming calculator for functions 
from time import time
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.8f}s')
        return result
    return wrap_func

# another way 
import timeit
def timer_func_v2(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        stop = timeit.default_timer()
        print(f'Function {func.__name__!r} executed in {(stop-start):.8f}s')
        return result
    return wrap_func