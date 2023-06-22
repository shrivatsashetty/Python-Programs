class VotingSystem(Exception):
    def __init__(self,name,id,age):
        super().__init__()
        self.name=name
        self.id=id
        self.age=age

try:
    name=input("Enter voter name:")
    id=int(input("Enter ID:"))
    age=int(input("Enter age:"))
    if age < 18:
        raise VotingSystem(name,id,age)
    voter1=VotingSystem(name,id,age)
    print("Eligible to vote")

except:
    print("Sorry you are not eligible to vote")
