list1=[2,4,"shri",'%','&',"vk@18",True]
print(list1)
print(list1[2]) #first op idexing
print(list1[-5]) #first op indexing
print(list1[2:5]) #second op slicing
print("initial list",list1)
list1.append(31)
print("after append",list1)# third op append
print("final list is",list1)
list2=[2,7,"Geography"]
list1.extend(list2) # fourth op extend/ join two list
print("list1 is now:",list1)
print("list2 is",list2)
list1[2]="Python" #fifith op mutation
print("list1 is now:",list1)
del list1[6] #6th op deleting item in list
print("del index 6 list1 is now:",list1)
del list1[7:9] # op 7
print("del from 6-9",list1)
list1.remove('&') # op 8
print("after removing '&'",list1)
print("list 2 is initially",list2)
list2.clear()#op 9
print("after clearing list 2 is",list2)
print("orignal list 1 is",list1)
list1.insert(2,'Java')
list1.reverse() #op 10 reverse
print("reversed list 1 is ",list1)
print("no of elements in list 1 is",len(list1))# op 11
print("after inserting java",list1)#op 12
print("count of no two is ",list1.count(2))
