def gen_func():
    # n=int(input("enter range:"))
    for i in range(10):
        yield i

catch_value = gen_func()


print(next(catch_value))
print(next(catch_value))

print(catch_value)
print(type(catch_value))
