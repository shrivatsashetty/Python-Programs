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

class Developer(Employee):
    increment=2.5
    def promotion(self):
        self.salary*=self.increment

class Manager(Employee):
    increment=3.5
    def promotion(self):
        self.salary*=self.increment
