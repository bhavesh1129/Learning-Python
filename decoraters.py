import time

def cache(func):
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return str(cache_value[args]) + " its cached value"
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(2)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(3,3))

