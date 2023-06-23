# arbirary argumnets
def polynomial_function(*variables):
    result=variables[0]**2+variables[1]*variables[0]
    print(result)

polynomial_function(2,3,4,5.6)