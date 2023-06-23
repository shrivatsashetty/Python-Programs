# ask name continiously, exit if user enter quit
val=True
while(val):
    name=input("Enter name:")
    if name==("quit" or "QUIT" or "Quit"):
        print("Exited")
        val=False
    else:
        print("Hello",name)
