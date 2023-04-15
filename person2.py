class people:
    name="no_name"
    age=0
    profession="citizen"
    siblings=["",""]
    def about(self):
        print(f"""about Mr.{self.name}:age:{self.age},works as:{self.profession},sibling:
        {self.siblings}""")

def main():  
    p1=people()
    p1.name=input("Enter the name of person:")
    p1.age=int(input("Enter his/her age:"))
    p1.profession=input("Enter proffession:")
    p1.siblings=input("names of siblings seperated by comma(,): ").split(",")
    p1.about()
