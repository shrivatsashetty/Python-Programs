while (True):
    print("1.List")
    print("2.Set")
    print("Exit")
    choice = int(input("Enter choice : "))
    if (choice == 1):
        l = []
        n = int(input("Enter range"))
        print("Enter the elements\n")
        for i in range(0, n):
            l.append(int(input()))
        print("list is ", l)
        while True:
            print("1.append 2.insert 3.pop 4.remove 5.reverse")
            ch = int(input("Enter the choice"))
            if ch == 1:
                e = int(input("Enter ele"))
                l.append(e)
                print("ele", e, "is appended successsfully")
                print(l)
            elif ch == 2:
                e = int(input("Enter ele"))
                p = int(input("Enter position"))
                l.insert(p, e)
                print(e, "is inserted at ", p)
                print(l)
            elif ch == 3:
                print("popped ele=", l.pop())
                print(l)
            elif ch == 4:
                v = int(input("Enter value to remove"))
                l.remove(v)
                print(l)
            elif ch == 5:
                l.reverse()
                print(l)
            else:
                break
        print()
    elif(choice == 2):
        while(True):
            print("1.size of set")
            print("2.add of set")
            print("3.check for a element of set")
            print("4.pop of set")
            print("5.clearing of set")
            print("0.exit")
            ch=int(input("enter your choice"))
            if ch==1:
                set1=set(input("enter the set"))
                print(set1._sizeof_())
            elif ch==2:
                set1=set(input("enter the set"))
                set1.add(7)
                print(set1)
            elif ch==3:
                set1=set(input("enter the set"))
                print(set1._contains_(8))
            elif ch==4:
                set1=set(input("enter the set"))
                set1.pop()
            elif ch==5:
                set1=set(input("enter the set"))
                set1.clear()
            else:
                break
    else:
        break