class person:
    name="noname"
    age=0
    job="Jobless"
    def __init__(self,n,a,j):
        print("Hello")
        self.name=n
        self.age=a
        self.job=j
    def info(self):
         print(f"{self.name},{self.age},{self.occupation}")
p1=person()
a=person(n="kishor",a=30,j="banker") 
# a.name="Kishor"
# a.age=30
# occupation="Banker"
a.info()