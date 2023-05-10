class CustomException(Exception):
    def __init__(self,mssg):
        print(mssg)

try:
    raise CustomException("This is a custom exception")
except:
    print("printing from except block")
    print("Exception handeled")
    