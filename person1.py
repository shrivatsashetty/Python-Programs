class Person:
   name = "I have no name :("
   def sayName(self):
      print("My name is...", self.name)

def main():
   aPerson = Person()
   aPerson.sayName()
   aPerson.name = "Big Smiley :D"
   aPerson.sayName()

main()