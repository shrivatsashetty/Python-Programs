"In this program we create initaialize an object inside a class"

class Main:
    attr1 = 2
    attr2 = 3
    
    def main(self):
        obj1 = Main()
        print(obj1.attr2)


myObj = Main()
print(myObj.attr1) # 2
myObj.main() # 3
