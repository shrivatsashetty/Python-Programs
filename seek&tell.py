f=open("myfile2.txt","r")

print(f.tell())
f.seek(25) # (25,0)
data=f.read()

print(data)
print(f.tell())