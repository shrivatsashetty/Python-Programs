f1 = open('myfile2.txt','r+')
f1.write("we can write to a file\nusing w+ mode")

content = f1.read()
print(content)


f1.seek(10,0)
content = f1.read()
print(content) 

