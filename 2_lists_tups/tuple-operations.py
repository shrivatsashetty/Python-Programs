#creating a tuple without ()
my_tuple=1,2.3,"hello",'#',True
print(my_tuple)
print(my_tuple[0])# (1, 2.3, 'hello', '#', True)
try:
    my_tuple[0]=2
except Exception as e:
    print(e)
    print("Tuple is immutable")
collection=tuple([3.14,'Hello','namaste',[1,2,3],(3,)])

# iterating over ordered pairs in nested tuple

nest = ((1,2),(3,4),(4,5),(5,6))

for x,y in nest:
    print(x,"maps to ",y)