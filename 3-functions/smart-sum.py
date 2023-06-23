def squre_adder(input_function):
    def square(a,b):
        a_squared=a**2
        b_squared=b**2
        sum=input_function(a_squared,b_squared)
        print(f"sum of squares of {a},{b} is",sum)
        return sum
    return square


@squre_adder
def summation(a,b): # this summation function itself becomes the input function
    return a+b

summation(int(input("Enter first number:")),int(input("Enter second number:")))


### with try except block

try:
    m=int(input("Enter an integer:"))
except ValueError:
    print("The value expected is an integer")
    m=0

try:
    n=int(input("Enter another integer:"))
except ValueError:
    print("The value expected is an integer")
    n=0

summation(m,n)