qty = [5,4,7,3,6,2,1]
print("Orignal list\n",qty,"\n")

newlist = qty.copy()
newlist.append(8)
print(newlist)

newlist = qty.copy()
newlist.insert(0,9)
newlist = qty.copy()
print(newlist)

newlist=qty.copy()
newlist.insert(3,8)
print(newlist)

newlist = qty.copy()
newlist.remove(newlist[0])
print(newlist)

newlist = qty.copy()
newlist.pop()
print(newlist)
########### or #############
newlist = qty.copy()
del newlist[len(newlist)-1]
print(newlist)

newlist = qty.copy()
del newlist[3]
print(newlist)

newlist = qty.copy()
newlist=newlist[::-1]
print(newlist)
######## or ##########
newlist = qty.copy()
newlist.reverse()
print(newlist)

newlist = qty.copy()
newlist.clear()
print(newlist)




