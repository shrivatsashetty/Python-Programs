names=['Suresh','Ramesh','Bharath','Naveen','Prakasha']

duplicate = names.copy()

print("the list is ",duplicate)

duplicate.append("Satish")
print(duplicate)     

duplicate = names.copy()
shortlist = duplicate[1:4]
print(shortlist)

duplicate = names.copy()
duplicate.remove(names[1])
print(duplicate)

duplicate = names.copy()
cutlist = duplicate[4:2:-1]
print(cutlist)