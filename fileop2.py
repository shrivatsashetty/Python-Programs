try:
    f1=open("veggies.txt","r")
    f2=open("fruits.txt","r")
    print(f1.read())
    print("Now printing line by line")
    # print(f2.readline())
    # print(f2.readline())
    # using for loop 
    for i in range(0,4):
        print(f2.readline())
    print("No error occoured")
except Exception as error:
    print(error)

print("Last")
