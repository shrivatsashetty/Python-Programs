class student:
    name="no_name" #Comment the attributes and the code still works same
    age=0          # Becoz in __init__ method the attributes are dynamically declared
    graduation="Degree" 
    def __init__(self):
        self.name=input("Enter the name of the student: ")#here name attribute is also dinamically created 
        self.age=int(input("enter Age:"))                                             #if not declared before
        self.graduation=input("enter Degree:")
    def info(self):    
        print(f"\nstudent'{self.name}'is {self.age}years old and has completed his {self.graduation}")                                  
s1=student()
s2=student()
s1.info()
s2.info()