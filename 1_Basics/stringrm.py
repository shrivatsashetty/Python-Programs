# Program to delete first n letters of a string

mystr="RVCE MCA DEPARTMENT"
print("The String:",mystr)
print("The no of characters:",len(mystr))

n=int(input("Enter how many letters to remove from start:"))
newstr=mystr[n:len(mystr)]
print(f"after removing starting {n} letter the string becomes:\n{newstr}")

