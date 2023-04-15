age=int(input("Plz enter you age"))
if age>=18:
    print("you are an adult")
elif age<18 and age>12 : # ':' indicates a block of statement below elif which is in indentation
    print("you are a teenger") # an indentation in the begining indicates that this block of code
else :                         # belongs to elif loop
    print("You are still a child")
print("thank you")