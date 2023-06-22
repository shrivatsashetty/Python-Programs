class A:
    name="Some Name"
    age=50
    location="Some place"
    def info(self):
        print(f"My name:{self.name},i live in {self.location}")
        print("Hello parent")
class child1(A):
    job="Developer"
class child2(A):
    job="farmer"

childobj1=child1()
childobj2=child2()
childobj1.info()
childobj2.info()

