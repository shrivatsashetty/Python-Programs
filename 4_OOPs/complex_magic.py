class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def __add__(self,other):
        sum=complex(0,0)
        sum.real=self.real+other.real
        sum.img=self.img+other.img
        return sum
    
    def __str__(self):
        return f"{self.real} + {self.img}i"
    
z1=complex(3,2)
z2=complex(3,5)

result=z1+z2
print(result)
