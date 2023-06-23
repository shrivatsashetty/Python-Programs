class MarksError(Exception):
    def __init__(self,mssg):
        print(mssg)

marks=float(input("Enter marks in entrance:"))
if(marks < 50):
    try:
        raise MarksError("Sorry, Not Qualified")
    except:
        print("Try again next time")
elif(marks > 100):
    raise MarksError("Marks cannot be more than 100")

else:
    print("Quiliifed")
    