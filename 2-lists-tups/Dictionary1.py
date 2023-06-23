person = {"name" : "Atul Bhat", "age" : 29, "Employed" : True, "Job" : "Teacher", "Salary" : 55000}

print(person)

person["age"] = 31 # updating
print(person)

del person["Salary"] # deleting an element
print(person)

person["Majors"] = "Physics" # added new element
print(person)

person.pop("age")
print(person)

map = person.items()
print(map) # dict_items([('name', 'Atul Bhat'), ('Employed', True), ('Job', 'Teacher'), ('Majors', 'Physics')])
print(type(map))

data =person.values()
print(data) # dict_values(['Atul Bhat', True, 'Teacher', 'Physics'])

print(list(data))

for key in person:
    print(key," : ",person[key])


