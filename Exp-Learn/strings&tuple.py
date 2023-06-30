while(True):
    print("1. String")
    print("2. Tuple")
    print("0. Exit")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        while(True):
            str = input("Enter the string : ")
            print("1. rindex")
            print("2. startwith")
            print("3. triple")
            print("4. isspace")
            print("5. is alphanumeric")
            print("0. Back 2 Menu")
            c = int(input("Enter your choice : "))
            if(c==1):
                i = input("Enter the character : ")
                print(str.rindex(i))# finds last occurance of a string
            elif(c==2):
                prefix = input("Enter The start with prefix : ")
                print(str.startswith(prefix))
            elif(c==3):
                print(3*str)
            elif(c==4):
                print(str.isspace())
            elif(c==5):
                print(str.isalnum())# alpha-numeric
            else:
                break
    if(choice==2):
        while(True):
            print("1. Sort")
            print("2. Reverse")
            print("3. Join")
            print("4. Check element")
            print("5. Compare Tuple")
            print("0. Back 2 Menu")
            c = int(input("Enter your choice : "))
            if(c==1):
                tup = tuple(input("Enter tuple elements : ").split())
                print(sorted(tup))
            elif(c==2):
                tup = tuple(input("Enter tuple elements : ").split())
                print(tuple(reversed(sorted(tup))))
            elif(c==3):
                tup = tuple(input("Enter tuple elements : ").split())
                print("|".join(tup))
            elif(c==4):
                tup = tuple(input("Enter tuple elements : ").split())
                n = input("Enter element to check : ")
                print(n in tup)
            elif(c==5):
                tup = tuple(input("Enter tuple elements : ").split())
                tup2 = tuple(input("Enter elements of tuple 2 : ").split())
                if(tup2 == tup):
                    print(f"both tuples are same")
                else:
                    print(f"The tuples are different")
            else:
                break
    else:        
        break