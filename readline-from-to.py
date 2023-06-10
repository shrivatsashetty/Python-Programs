# print the file from line 5th onwards to line 9th 

f = open('fruits.txt','rt')

n = int(input("Enter start line:")) 
m = int(input("Enter end line:"))


for i in range(1,m+1):
    if i<n:
        content=f.readline()
        continue
    content=f.readline()
    print(content)

# 'content' variable can posiibly be unbound i.e for loop could run zero times

##########old version of this code ###############
 
# n = int(input("Enter start line:")) 
# m = int(input("Enter end line:"))

# for i in range(1,n):
#     content=f.readline()

# for i in range(n,m+1):
#     content=f.readline()
#     print(content)
