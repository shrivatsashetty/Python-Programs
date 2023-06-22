class People:
   name = "Nameless"
   age=0

   def __init__(self, a="no_name",b=10): # arg b is set to def val 17
       self.name = a
       self.age=b
       print(f"Name is:'{self.name}',age is {self.age} \n")


Person1 = People(b=int(input("Enter age:")),a="James Cameron")
Person2 = People("Louis Philippe",67)
Person3 = People("Michael Jonson")
Person4 = People()
Person5 = People(a=input("Enter Person5 name:"),b=int(input("Enter Person5 age:")))
Person6 = People(a=int(input("Enter Person6's age instead of name:")),b=input("Enter Person6's Name instead of age:"))
print("\n print from outside class method:",Person1.name)
