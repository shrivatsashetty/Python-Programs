class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self,other):
        vector_sum=Vector(0,0)
        vector_sum.x = self.x + other.x
        vector_sum.y = self.y + other.y
        return vector_sum

    def __len__(self):
        return int((self.x**2 + self.y**2)**(0.5)) # len method is always used to return a integer value
    
    def __str__(self):
        return f"Vector: ({self.x},{self.y})" # a string desvcription of the vector object
    
v1=Vector(3,4)
v2=Vector(1,5)
resultant = v1 + v2
print(resultant)
print(len(resultant))
