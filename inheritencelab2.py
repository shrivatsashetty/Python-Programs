d={}
class Student:
    def __init__(self):
        self.name=input("Enter name:")
        self.usn=input("Enter USN:")
        self.age=int(input("Enter age:"))
    def displayinfo(self):
        print("Name:",self.name)
        print("USN:",self.usn)
        print("age:",self.age)
class derived1(Student):
    def __init__(self):
        Student.__init__(self)
        self.sem=int(input("Enter sem:"))
        self.marks=[]
        self.total=0
        for i in range(5):
            score=float(input("Enter marks:"))
            self.marks.append(score)
            self.total+=score
        self.percentage=((self.total/(500))*100)
    def displayinfo(self):
        derived1().displayinfo()
        print("Semester:",self.sem)
        for i in range(5):
            print(f"marks in sub{i+1}={self.marks[i]}")
        print("Percentage is",self.percentage)

class derived2(derived1):
    def __init__(self):
        derived1.__init__(self)
        d.update({self.name:{
            "Name":self.name,
            "USN":self.usn,
            "age":self.age,
            "semester":self.sem,
            "Marks":self.marks,
            "Total":self.total,
            "percentage":self.percentage
        }})
def printinfo():
    for field in d:
        print(field,":",d[field])
# while True:
print(" 1.Addinfo \n 2.Showinfo \n 3.Exit\n")
ch=int(input("Enter a Choice"))
if ch==1:
    std=derived2()
elif ch==2:
    printinfo()
