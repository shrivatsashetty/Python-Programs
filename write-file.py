f1=open("test.txt","w")
f1.write("Some line in my mind\n")
f1.close()
f1=open("test.txt","r")
print(f1.read())
f1.close
f2=open("test.txt","a")
f2.write("appended lines")
