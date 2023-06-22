even=[2,4,6,8,10,12]
print(even[2:6])
for num in even:
    print(num)
even.append(14) # a new element is being appended to end of the list even
print(even)
even.insert(0,0)
print(even)
print("no of elements in the list is",len(even))
i=0
while i < len(even):
    print(i,"th elements of list is",even[i])
    i=i+1
empty=even.clear()
print(empty)
print(even)

