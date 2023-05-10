# this program demontrates the concept of Exception as well as Recursion
def handle():
    try:
        n=int(input("Enter a number:"))
        print("The no u entered is",n)
    except Exception as a:# 'Exception' is a keyword
        print(a)
        print("Enter only an integer number as input")
        handle() # The function is recursing

handle()

print("program sucessfully completed\n======THE END======")