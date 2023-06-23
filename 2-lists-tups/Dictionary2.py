marks = {'Physics':67, 'Maths':87}
print(marks)

internal_marks = {'Practical':48}
marks.update(internal_marks)
print(marks)

marks.update({"Biology":89})
print(marks)

extra_ciriculars = {'Sport' : 95, 'NCC' : "Navy"}

marks.update(extra_ciriculars)
print(marks)

for key,value in marks.items():
    print(f"Score in {key} is {value}") 