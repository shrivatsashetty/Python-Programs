sum = lambda x,y: x+y

print(sum(2,3)) # 5

print(sum) # <function <lambda> at 0x7fc081127d90>

greet = lambda: print("Hi World")
greet()

polynomial_function = lambda x=0,y=0,z=0: 2*x+y+z+3*x*z # takes default arguments, if not conveyed explicitly
result = polynomial_function(1,2,3)
print(result)
