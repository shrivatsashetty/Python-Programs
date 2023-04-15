print("======TUPLE OPERATION=========")
tup = tuple(input("Enter the tuple \n").split())

while True:
    print(" 1.Concatenation\n 2.Nested \n 3.type \n 4.Reverse \n 5.slice \n 6.find \n 7.length \n 8.count \n 9.min\n 10.max \n 11.exit \n")

    a = int(input("Enter your choice \n"))

    if a == 1:
        tup1 = tuple(input("Enter another tuple \n").split())
        print(tup + tup1)

    elif a == 2:
        tup2 = tuple(input("Enter another tuple \n").split())
        print((tup,) + (tup2,))

    elif a == 3:
        print(type(tup))

    elif a == 4:
        print("Reverse tuple :-", tup[::-1])

    elif a == 5:

        b = int(input("Enter start index no.\n"))
        c = int(input("Enter last index no. \n"))
        print("Slicing :-", tup[b:c])

    elif a == 6:
        d = int(input("Enter the index of element that u want to check \n"))
        print(tup[d])

    elif a == 7:
        print("Length :-", len(tup))

    elif a == 8:
        e = input("Enter the element that u want to check how many times..\n")
        print(tup.count(e))

    elif a == 9:
        print("Minimum:-", min(tup))

    elif a == 10:
        print("Maximum :-", max(tup))

    elif a == 11:
        print("=====End of operation=======")
        exit()

    else:
        break
