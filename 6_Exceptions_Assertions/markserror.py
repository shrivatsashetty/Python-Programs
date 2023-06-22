# Base Class, this class acts like Distributor of inbuilt Exception class
class MarksError(Exception):
    pass
# all below class inherit from Distributor class

# exception for percentage >100
class InvalidMarksError(MarksError):
    def __init__(self):
        super().__init__("Invalid Marks")

# exception class for marks less than 60
class LessMarksError(MarksError):
    def __init__(self):
        super().__init__("The marks is less than minimum marks, Plz try next time")
        #the __init__ method of parent class actually prints the text passesd as argument

# class to check percentage range
class CheckMarks(MarksError):
    def __init__(self,per):
        if per < 60:
            raise LessMarksError
        elif per > 100:
            raise InvalidMarksError
        else:
            print("Congrats you are admitted")

# differet cases
try:
    print("For marks:90 ")
    CheckMarks(90)
except Exception as e:
    print(e)

try:
    print("\nFor Marks: 105")
    CheckMarks(105)
except Exception as e:
    print(e)

try:
    print("\nFor Marks: 56")
    CheckMarks(56)
except Exception as e:
    print(e)
    
# in this program we can also choose not to use the Distributer class 
# Instead directly inherit from inbuilt Exception class
# But due to some reason not reccomended
        
