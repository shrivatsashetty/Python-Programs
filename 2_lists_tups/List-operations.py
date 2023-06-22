# lists are mutable, and can store items of different data type
while(1):
    print("1.List operations\n2.Extend list\n3.Exit")
    ch=int(input("Enter a choice:"))
    if (ch==1):
        languages=["Kannada","Hindi","English","Tulu","Konkani"]
        print(languages[2])# English
        print(languages[-2])# Tulu, i.e second item from last
        # print(languages[5]) # out of index, raises index error
        numbers=[1,2,3,4,5,6,7]
        print(len(numbers))# 7
        numbers.append(8)# 8 is appended at last
        print(numbers)# [1, 2, 3, 4, 5, 6, 7, 8]
        print(type(numbers))# <class 'list'>
        mixture=list(("Karnataka",1,True,False,[1,2,3]))# list() constructor
        print(mixture)
        #copying the list
        numbers_copy=numbers.copy()
        print(numbers_copy)# [1, 2, 3, 4, 5, 6, 7, 8]
        scores_of_batsmen=[1,2,1,3,3,5,7,1,10,5,2]
        print(scores_of_batsmen.count(1))# 3 ,since 1 is repeated 3 times in the list
        languages.insert(1,"Tamil")# ['Kannada', 'Tamil', 'Hindi', 'English', 'Tulu', 'Konkani']
        print(languages)
        languages.pop(3)# removes element at specified index
        print(languages)# ['Kannada', 'Tamil', 'Hindi', 'Tulu', 'Konkani']
        languages.remove('Tamil')# removes specified item, 'Tamil' is removed here
        print(languages)# ['Kannada', 'Hindi', 'Tulu', 'Konkani']
        mixture.remove(False)
        print(mixture)# ['Karnataka', 1, True, [1, 2, 3]]
        numbers.reverse()# reverses the list
        print(numbers)# [8, 7, 6, 5, 4, 3, 2, 1]
        numbers.sort()# [1, 2, 3, 4, 5, 6, 7, 8]
        print(numbers)
        # using del()
        del numbers[0]# for del() we use index
        print(numbers)
        del numbers[3:5]
        print(numbers)# [2, 3, 4, 7, 8]

    elif(ch==2):
        # joining two list
        lst1=[]
        lst2=[]
        n1=int(input("Enter the no of elements in your first list:"))
        for i in range(0,n1):
            element=input(f"Enter {i+1}th element:")
            lst1.append(element)
        print(lst1)
        n2=int(input("Enter the no of elements in your second list:"))
        for i in range(0,n2):
            element=input(f"Enter {i+1}th element:")
            lst2.append(element)
        print(lst2)
        lst1.extend(lst2)
        print(f"new list:{lst1}")
    elif(ch==3):
        break
    else:
        print("Enter a valid input")


