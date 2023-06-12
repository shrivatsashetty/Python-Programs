# method overloading 

class calci:
    def addition(self,a,b=0,c=0):
        print("sum is :",a+b+c)
        return a+b+c
    
obj1 = calci()

obj1.addition(1)
obj1.addition(1,2)
obj1.addition(1,2,3)
