f=open("myfile2.txt","r")

data=f.readlines()


for x in data[2:] :
    print(x)