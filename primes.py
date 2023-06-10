n = int(input("Enter a number:"))

if n <= 1:
    print("No primes in this range")

for numbers in range(1,n):
    for factors in range(1,numbers):
        
        if ((factors != 1 and factors != numbers) and numbers % factors == 0):
            print(numbers,"is prime")
        else :
            print(numbers,"is composite")