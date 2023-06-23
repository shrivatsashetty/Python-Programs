class Myclass:
    attr1=20
    attr2="This is attribute 2"
obj1=Myclass()

print("Class attribute-1:",Myclass.attr1)
print("Class atribute-2",Myclass.attr2)
print(f"object attribute-1 : {obj1.attr1}")
obj1.attr1=30
print("Updated object attribute 1:",obj1.attr1)
print("class atribute 1 is still:",Myclass.attr1)