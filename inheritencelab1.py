class STUDENT:
    def __init__(self):
        self.name=input("Enter student name:")
        self.USN=input("Enter USN:")
        self.age=int(input("Enter age of student:"))
    def displayinfo(self):
        print("Name:",self.name)
        print(f"USN:{self.USN}")
        print(f"Age:{self.age}")

class PGSTUDENT(STUDENT):
    def __init__(self):
        STUDENT.__init__(self)
        self.sem=int(input("Enter Semester of study:"))
        self.fees=float(input("Enter anual fees:"))
        self.stipend=float(input("Enter stipend:"))
        PGSTUDENT.displayinfo
    def displayinfo(self):
        print(f"semester of study:{self.sem}")
        print(f"Anual fees :{self.fees}")
        print(f"stipend earned:{self.stipend}")

Shrivatsa=PGSTUDENT()
Shrivatsa.displayinfo()