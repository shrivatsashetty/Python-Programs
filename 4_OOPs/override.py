class Employee:
    def __init__(self):
        self.name=input("Enter Name: ")
        self.age=int(input("Enter age: "))
        self.salary=float(input("Enter salary: "))
    def promotion(self):
        self.salary*=1.25
        print(f"{self.name}'s salary after promotion is {self.salary}")

class Developer(Employee):
    def promotion(self):
        self.salary*=1.5
        print(f"{self.name}'s salary after promotion is {self.salary}")

class Manager(Employee):
    def promotion(self):
        self.salary*=2
        print(f"{self.name}'s salary after promotion is {self.salary}")

choice=int(input("Enter a choice: "))
if choice==1:
    emp1=Employee()
    emp1.promotion()
elif choice==2:
    dev1=Developer()
    dev1.promotion()
elif choice==3:
    man1=Manager()
    man1.promotion()



