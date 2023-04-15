class human:
    age=10 # default value for age attribute is 10
    name="Some name" # def val for name attr is "some name"

person1=human() #person1 belongs to human class
print(person1.name) #default value of name attribute gets printed 
person1.name="sumanth" #name value gets updated
print(person1.name,person1.age)
person1.age=54
 #updated name value is printed
# print(person1.name)