#program for a simple calculator
op=input("Enter the operation to be performed: ")
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
if op=='+':
    print("a + b = ",a+b)
elif op=='-':
    print("a - b = ",a-b)
elif op=='x':
    print("a x b = ",a*b)
elif op=='/':
    print("a / b = ",a/b)
elif op=='mod':
    print("remainder obtained in division a/b is",a%b)
elif op=='^':
    print("a raised to power b is",a**b)
elif op=='q' :
    print("a divided by b gives a qoutient",a//b)
else :
    print("operation unknown")
print("thank you for using python calculator")