class Person:
   name = "I have no name :("
   def sayName(self):
      print("My name is...", self.name)

def main():
   mary = Person()
   mary.name = "Mary james, nice to meet you."
   james = Person()
   james.name = "I'm james, who are you???!!!"

   mary.sayName()
   james.sayName()

main()
