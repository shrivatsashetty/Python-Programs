class operation():
    def __init__(self):
        self.l1=[]
        self.input()

    def input(self):
        n = int(input("Enter no of ele:"))
        for i in range(n):
            ele=int(input("Enter element:"))
            self.l1.append(ele)
        print(self.l1)
    
    def __add__(self,other):
        self.result=[]
        for i in range(len(self.l1)):
            self.result.append(self.l1[i] + other.l1[i])
        print("After adding list:",self.result)

ob1=operation()
ob2=operation()
print(ob1+ob2)
# print(ob1)