import time


def cache(func):
    cahce_value = {}
    print(cahce_value)

    def wrapper(*args, **kwargs):
        if args in cahce_value:
            return cahce_value[args]
        result = func(*args, **kwargs)
        cahce_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(1, 2))
print(long_running_function(1, 2))
print(long_running_function(3, 2))
