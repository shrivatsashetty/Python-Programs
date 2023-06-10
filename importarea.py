from areasofshapes import *
while(True):
    
    print("1.Rectangle\n2.Square\n3.Circle\n4.Triangle\n0.Exit")
    opt = int(input("Choose an option:"))
    if opt == 1:
        l=float(input("Enter length of rectangle:"))
        b=float(input("Enter width rectangle:"))
        arearect(l,b)
    elif opt == 2:
        l = float(input("Enter side of the square:"))
        areasquare(l)
    elif opt == 3:
        radius = float(input("Enter radius of the circle:"))
        areacircle(radius)
    elif opt == 4 :
        base = float(input("Enter base length: "))
        height = float(input("Enter height:"))
        areatriangle(base,height)
    elif opt == 0:
        break
    else:
        print("Invalid input")

