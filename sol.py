def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key, value in kwargs.items())

        print(f"Calling {func.__name__} with arguments {args_value}, and key arguments {kwargs_value}")
        
        return func(*args, **kwargs)
    return wrapper

# DECORATERS
# def debugExample(funcExample):
#    def wrapperExample(**arge, **kwargs):
#
#        // logic
#
#        return funcExample(*args, **kwargs)
#   return wrapperExample
#
# @debugExample


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet(name="Rahul", greeting="hanji")
