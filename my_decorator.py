def my_decorator(original_function):
    def new_function():
        print("Before the function is called.")
        original_function()
        print("After the function is called.")
    return new_function

@my_decorator
def my_function():
    print("my_function is called now.")

my_function()