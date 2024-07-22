""" A Python Program to print prime numbers in a given range """

start = 1
end = 10

for num in range(start, end):

    for factor in range(2,num):
        
        if (num % factor == 0):
            continue
        else:
            print(num)