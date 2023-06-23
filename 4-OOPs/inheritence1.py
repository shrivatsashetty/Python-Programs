class Parent1:
    def pmethod1(self):
        print("Hi from Parent 1")
class Parent2:
    def pmethod2(self):
        print("hi from parent 2")
class Child(Parent1,Parent2):
    def cmethod1(self):
            print("hello from child")

child1=Child()
child1.pmethod1()
child1.pmethod2()
child1.cmethod1()