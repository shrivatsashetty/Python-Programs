numbers=[1,2,3,4,5]

double = lambda x : 2*x

doubled_numbers = map(double,numbers)

print(doubled_numbers)

print("Doubled no's:",list(doubled_numbers))

squared_numbers=map(lambda x:x**2,numbers)
print("Squared no's:",list(squared_numbers))

def cube(x):
    return x**3

cubed_numbers=map(cube,numbers)
print("cubed no's:",tuple(cubed_numbers))
