class MyContext:
    def __init__(self):
        print("init method is called")

    def __enter__(self):
        print("enter method is called")

    def __exit__(self,exec,b,c,):
        print("exit method is called, rescource cleaned")

obj=MyContext()

with obj as rescource:
    print("Rescourses are being consumed")
    print(rescource)




