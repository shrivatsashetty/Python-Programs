def div(a,b):
    try:
        result=a/b
        print(result)
        return "no exception"
    # this except block handles only ZeroDivisionError
    except ZeroDivisionError:
        print("Cant divde a number by zero")
    # This Excecption can handle any type of exceptions in general
    except Exception as error:
        print(error)
        mssg="try again"
        print(mssg)
        return mssg
    # This statement will get printed anyways
    finally:
        print("Handled the exception")

div(1,2)
div("w",4)
div(2,0)

print("=====End=====")


    