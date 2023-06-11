f = open('myfile2.txt','r+')
content = f.readline()
print(content)

print(f.tell())
f.seek(0,0)
print(f.tell())
count=0
for i in range(2):
    f.readline()
    count+=1
print("Line read:", count)
print("Characters read:",f.tell())

print("from 3rd line onwards")


data = f.readlines()
print("lines to be read:",data)
for lines in data:
    print(lines)


f.seek(0,0)
data = f.readlines()
print("From 3rd line to 7th\n",data[:7])
for lines in data[2:7]:
    print(lines) 
