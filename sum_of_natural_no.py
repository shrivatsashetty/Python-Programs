#program to calculate sum of first n natural no
n=int(input("Enter a natural number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of first",n,"natural no's:",sum)
