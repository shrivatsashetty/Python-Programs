#class is like a basic structure for an object.like for example,"cat" is a calss containing objects lion,tiger,cheethah etc
#this class contains attributes like no of teeth,no of nails,habitat,height,size,running speed etc
#when we define a class we also set default values for each attribute
#consider a class called employee,all people(objects) having a job come under this class and every one of them have certiain common set of character(attributes)

class employee: 
    name="something"
    age=25
    salary=4.5
    native="Bangalore"
    def info(self):
        print(self.name,"is an employee whose anual income is",self.salary)

naveen=employee() #indicates,variable "naveen" is an object coming under employee class 
naveen.name="naveen"
naveen.salary=float(input("How much would u salary naveen anually:"))
naveen.native="Mangaluru"
print("the employees name is:",naveen.name)
print("naveens anual package is",naveen.salary)
print("Naveen is ",naveen.age,"yrs old")
print("naveens native place is:",naveen.native)
    