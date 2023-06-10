# first step to do any file opeartion is to open it

f=open('myfile3.txt',"r")
line = f.readline()
print(line)  # first line is printed 

line = f.readline()
print(line)  # second line is printed

# the readline() method does not read the content already read 

# using for loop we can print all the lines 