#prog todisplay tables of a number
print("This program displays tables of a number")
a=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{a}x{i}={a*i}")