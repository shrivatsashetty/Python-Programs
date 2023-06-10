# 'rt' means read in text mode, 'rb' is read in binary
f1=open('myfile3.txt','rt')

content=f1.read(3) 
print(content)   #Thi

content=f1.read(3)# it will not read the already red content
print(content)   #s i

content=f1.read(100)
print(content)

