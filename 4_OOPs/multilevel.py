d={}
class student:
    def __init__(self):
        self.name=input("Enter name:")
        self.age=int(input("Enter age:"))
    def display(self):
        print("name:",self.name,"age:",self.age,)
    
class derived1(student):
    def __init__(self):
        super().__init__()
        self.sem=int(input("Sem: "))
        self.fees=float(input("Fees: "))
        self.marks=[]
        self.total=0
        for i in range(4):
            mark=int(input("marks: "))
            self.marks.append(mark)
            self.total+=mark
        self.percent = (self.total/4)
        

    def display(self):
        super().display()
        print("sem: ",self.sem)
        print("fess: ",self.fees)
        print("marks: ",self.marks)
        print("total: ",self.total)
        print("percent: ",self.percent)

class derived2(derived1):
    def __init__(self):
        super().__init__()
        d.update({self.name:{
                "name":self.name,
                "age":self.age,
                "sem":self.sem,
                "fees":self.fees,
                "marks":self.marks,
                "total":self.total,
                "percent":self.percent
        }})

def printstd():
    for key in d:
        print(key,d[key])

d2=derived2()
d2.display()
printstd()
