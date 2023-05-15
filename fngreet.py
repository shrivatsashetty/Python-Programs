# function without args
def greet():  #declaring a function
    name=input("Enter your name: ")
    print("hi",name)
    return name  #return indicates that the function has ended
greet() #calling a function
#functions with args
def addnums(x,y): # adnumms is function of arguments x and y
    sum=x+y       # defining what do with arguments i.e definition of function
    print("The sum of",x,"and",y,"is",sum)
num1=int(input("Enter first no:"))
num2=int(input("Enter second no:"))
addnums(num1,num2)
#same addition function without args
def addition():
    no1=float(input("Enter first no: "))
    no2=float(input("Enter second no: "))
    total=no1+no2
    print(no1,"+",no2,"=",total)
    return sum #return is not mandatory
addition()