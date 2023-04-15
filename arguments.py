def avg(a=10,b=20): # 10 and 20 are default values for a & b
    print(f"the average of {a},{b} is {(a+b)/2}")
c=float(input("Enter first number:"))
d=float(input("Enter second number:"))
avg(c,d)
avg(12)
avg(b=4)
avg(a=16)
avg(b=12,a=4)# here oredr of passing arguments does not matter
