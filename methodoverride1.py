class Employee:
    increment=1.5
    def __init__(self):
        self.firstname=input("Enter firstname:")
        self.lastname=input("Enter lastname:")
        self.empid=input("Enter employee ID:")
        self.salary=float(input("Enter salary:"))
    def displayinfo(self):
        print(f"First name:{self.firstname}")
        print(f"Last name:{self.lastname}")
        print(f"Employee ID:{self.empid}")
        print(f"Salary = {self.salary}")
    def promotion(self):
        self.salary*=self.increment
        print(f"salary of {self.firstname} is {self.salary}")

class Developer(Employee):
    increment=2.5
    def promotion(self):
        self.salary*=self.increment
        print(f"salary of {self.firstname} is {self.salary}")

class Manager(Employee):
    increment=3.5
    def promotion(self):
        self.salary*=self.increment
        print(f"Salary of{self.firstname} is {self.salary}")

e1=Employee()
d1=Developer()
m1=Manager()

e1.displayinfo()
e1.promotion()

d1.displayinfo()
d1.promotion()

m1.displayinfo()
m1.promotion()