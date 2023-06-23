class Person:
        # name=None 
        # age=None
        # you comment or uncomment above two lines,the program works the same
        def Hello(self, name=None,age=None):
                self.name=name
                self.age=age

                if (self.name==None and self.age==None): 
                        print("Hello")

                elif (self.name==name and self.age==None) :
                        print(f"Hello {self.name}")

                elif self.name==name and self.age==age : #in python no parenthesis is required for if or elif declaring test-condition
                        print(f"Hello {self.name} age:{self.age}")
                
p1=Person()
p1.Hello()
p1.Hello('GouthamAS')   
p1.Hello('GouthamAS',25)
p1.Hello(age=25,name='GauthamAS') # o/p is Hello GauthamAS age:25

