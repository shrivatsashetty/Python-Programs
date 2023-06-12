class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print( "__init__ method called" )
    def __str__(self):
        return f"person with age {self.age} & name {self.name}"
    def display(self):
        print(self.name,self.age)
    def __del__(self):
        print(f"Object {self.name} deleted")
    
obj=Person("Ajay",24)
obj.display()
print(obj)

del obj



    