class MarkError(Exception):
    pass

class ExcessMarkError(MarkError):
    def __init__(self):
        super().__init__("Marks cannot be greater than 100")
        
class LessMarkError(MarkError):
    def __init__(self):
        super().__init__("Sorry,Minimum marks of 60 not secured")
    
class CheckMarkError(MarkError):
    def __init__(self,marks):
        self.marks=marks
        if self.marks > 100:
            raise ExcessMarkError()
        elif self.marks < 60:
            raise LessMarkError()
        else:
            print("Congrats You are Admitted")
            
try:
    print("For 110 marks")
    more_score = CheckMarkError(110)
    print("You are addmitted")
except Exception as e:
    print(e)
    
try:
    print("For 55 marks")
    less_score = CheckMarkError(55)
    print("You are addmitted")
except Exception as e:
    print(e)
    
try:
    print("For 75 marks")
    perfect_score=CheckMarkError(75)
except Exception as e:
    print(e)
    
    
        