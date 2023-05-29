def gen_func():
    n=int(input("enter range:"))
    for i in range(n):
        yield i

# catch_value=gen_func()

for j in gen_func():
    print(j)
