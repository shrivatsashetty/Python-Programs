def myFun(*args):
    for item in args:
        print(item)

myFun("Hello","Hi","Bye-Bye")
myFun("namaste","Vanakkam")


def sum(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("\nSum:",sum)
    return sum

sum(1,2,3,4,5)