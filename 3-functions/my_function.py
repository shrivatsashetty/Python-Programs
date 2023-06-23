def my_function():
    print("my_function is called now.")

def my_decorator(func):
    print("Before the function is called.")
    def new_function():
        print("After the function is called.")
    func
    new_function()
    #return new_function

#@my_decorator


my_decorator(my_function())
#my_function()