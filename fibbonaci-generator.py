def fibbonaci():
    a,b=0,1
    while(1):
        yield a
        a, b = b, a+b

        
seq=fibbonaci()

n=int(input("Enter Iteration:"))
for i in range(n):
    print(next(seq))