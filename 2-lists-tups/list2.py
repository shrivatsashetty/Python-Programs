# animals list
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox','bear']

# combining wild_animals list to animals
animals.extend(wild_animals)
animals.append('Parrot')

print('Updated animals list: ', animals)# ['cat', 'dog', 'rabbit', 'tiger', 'fox', 'bear', 'Parrot']
print(animals.index('fox'))# 4