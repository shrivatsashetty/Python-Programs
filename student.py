class student:
    def __init__(self):
        self.usn=input("Enter USN: ")
        self.name=input("Enter Student name: ")
        self.age=int(input("Enter age: "))
    def display(self):
        print("student name is ",self.name)
        print("students age is ",self.age)
        print("Students USN is ",self.usn)
class ugstudent(student):
    def __init__(self):
        student.__init__(self)
        self.sem=int(input("Enter semester of study:"))
        self.fees=int(input("Enter course fee:"))
        self.stipend=float(input("Enter internship stipend:"))
        ugstudent.display(self)