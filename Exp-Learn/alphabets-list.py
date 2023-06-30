alpha=["a","b","A","d","I","H","o","K","e","u"]


newlist=[]
vowels=['a','e','i','o','u','A','E','I','O','U']
for character in alpha:
    if character in vowels:
        newlist.append(character)
print("The list got by extracting the vowels\n",newlist)

cutlist=alpha[7:1:-1] # slicing in reverse
print(cutlist)


