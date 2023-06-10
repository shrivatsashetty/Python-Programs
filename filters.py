# filter function to sort even and odd no's from a list

def is_even(a):
    return a%2==0

numbers=[1,2,3,4,5,6,7,8,9]

even_numbers=filter(is_even,numbers)
print("Even no's:",list(even_numbers))

is_odd=filter(lambda a:a%2!=0,numbers) # the function can also be a lambda
print("Odd no's",list(is_odd))