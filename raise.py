lst1=[1,2,3,4]
print(f"the list is {lst1}")

i=int(input("Enter an index:"))

if(i<0 or i>3):
    raise IndexError("No such index in the list")
    #print("oops, the index is not in range, try again")

else:
    print(f"The element at the index {i} is:",lst1[i])