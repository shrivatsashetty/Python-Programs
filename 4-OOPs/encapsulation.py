class MyClass:
    def __init__(self):
        self.public_variable = 6 
        self._protected_variable = 20
        self.__private_variable=45

    def display(self):
        print("Protected variable:",self._protected_variable)
        print("Private variable: ",self.__private_variable)


obj1 = MyClass()
print("Protected variable",obj1._protected_variable)  # Accessing protected variable (not recommended)

try:
    print("Private var: ",obj1.__private_variable)
    print("Private member accessed")
except AttributeError: # trying acess non accessible attribute
    # print("error:",e)
    print("Private member cannot be accesed from outside the class")

obj1.display()




