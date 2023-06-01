d={}
class Employee:
    def input(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.basic = float(input("Enter Base pay:"))
        self.deduct = float(input("Enter deduction:"))
        self.hra = 0.25*self.basic
        self.da = 0.30*self.basic
        self.gross = self.basic + self.hra + self.da
        self.netpay = self.gross - self.deduct
        self.update()
    def update(self):
        d.update({self.name:{
            "name":self.name,
            "age":self.age,
            "basic":self.basic,
            "deduct":self.deduct,
            "netpay":self.netpay
            }})
    def search(self,name):
        flag=0
        for key in d:
            if key == name:
                print("Match Found")
                for i in d[key]:
                    print(i,d[key][i])
                    flag=1
        if flag == 0:
            print("Employee not found")

    def printemp(self):
        for key in d:
            print(key,d[key])

emp=Employee()
while 1 :
    print(" ")
    ch=int(input("Enter choice:"))
    if ch == 1:
        emp.input()
    elif ch==2:
        emp.printemp()
    elif ch==3:
        name=input("Enter emp name:")
        emp.search(name)
    elif ch==0:
        break
