class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
           
    def __str__(self):
        return f"the object belong to {super().__class__.__name__} class\nname is {self.name},age is {self.age}"

p1=Person("Raj",36)
print(p1)