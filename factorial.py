#program to print factorial of a number
def fact(n):# 'n' is a local variable here, its scope is limited to fact() function
    result=1
    for number in range(1,n+1):
        result*=number
    print(f"{n}! is {result}")
    return result #now this function has a value = fact(n)
    
num=int(input("Enter a number for factorial:"))
fact(num)
print(f"The return value of fact({num}) function is:",fact(num))
seven_factorial=fact(7)
#storing return value of a function inside a variable
print(seven_factorial)