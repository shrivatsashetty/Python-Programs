def factorial(n):
    if(n==0 or n == 1):
        return 1
    elif(n<0):
        print("Please enter positive number.")
        return -1 # -1 is error code for wrong input
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number: "))
print(factorial(n))





