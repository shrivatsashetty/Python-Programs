class Animals:
    def __init__(self):
        self.life=True
        self.senses=["hear","sight","feel"]
    def sound(self):
        print("Animal sound...")
        
class Flyables(Animals):
    def fly(self):
        print("fly high in the sky")

class Mamals(Animals):
    def givebirth(self):
        print("Warm blooded & Dont lay eggs")

class Bats(Flyables,Mamals):
    def ecolocation(self):
        print("Ecolocation sound")

Horse=Animals()
Eagle=Flyables()
Humans=Mamals
VampireBat=Bats()

print(VampireBat.life)
print(VampireBat.senses)
VampireBat.sound()
VampireBat.fly()
VampireBat.givebirth()
VampireBat.ecolocation






