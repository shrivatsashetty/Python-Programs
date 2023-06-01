import time

def time_counter(func):
    def clock():
        print("before decorator")
        result=func()
        print("after decorators")
        return result
    return clock


@time_counter
def fibbonaci():
    a,b=0,1
    while(1):
        yield a
        a, b = b, a+b

        
seq=fibbonaci()

n=int(input("Enter Iteration:"))
for i in range(n):
    print(next(seq)) # fibbonacci is called here