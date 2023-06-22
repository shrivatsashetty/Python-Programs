# functions to calculate areas of some basic geometric shapes

def areasquare(l):
    print("area of the square:",l**2)
    return l**2

def arearect(l=0.0,b=0.0):
    print("area of rectangle:",l*b)
    return l*b

def areacircle(r):
    area = 3.14*r**2
    print("area of circle:",area)
    return area

def areatriangle(b,h):
    area = 0.5*(b*h)
    print("Area of the traingle:",area)
    return area

""" thing to remember is since this is a module we are going to import this to many other programs
so we should not call any of the functions in this program """  