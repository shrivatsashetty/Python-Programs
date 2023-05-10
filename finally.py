def func1():
    try:
        ls=[1,2,3,4]
        print("The list we have is \n",ls)
        n=int(input("Enter a number for index:"))
        print("integer u entered is:",n)
        print("Element @ given index is",ls[n])
        return "sucess"
    except:
        print("some exception occured")
        return "Error"
    finally:
        print("Printed from finally block")
        # if this print statement would not have been written in finally block
        # it would not have been executed

program_status=func1()
print("Program status:",program_status)
