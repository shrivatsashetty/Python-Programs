def log_function_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}. Result: {result}")
        return result
    return wrapper

@log_function_calls
def calculate_difference(a, b):
    return a - b

calculate_difference(b=7,a=5)
calculate_difference(6,2)
