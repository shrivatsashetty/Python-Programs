# first step to do any file opeartion is to open it

f=open('myfile3.txt',"r")
line = f.readline()
print(line)  # first line is printed 
line = f.readline()
print(line)  # second line is printed

# using for loop we can print all the lines 