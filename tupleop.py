print("======TUPLE OPERATION=======")
tup1=tuple(input("enter yor tuple \n").split())
while True:
    print("1.Concatenation\n2.Nested\n3.Type\n4.Reverse\n5.Slice\n6.Find\n7.Length\n8.Count\n9.Min\n10.Max\n11.exit")
    chc=int(input("Enter a choice"))

    if chc == 1:
        tup2=tuple(input("Enter another tuple").split())
        print(tup1+tup2)
    elif chc==2:
        tup2 = tuple(input("Enter another tuple").split())
        print((tup1,)+(tup2,))
    elif chc==3:
        print(type(tup1))
    elif chc==4:
