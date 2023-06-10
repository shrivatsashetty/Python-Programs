
def rangefunc(n):
    for i in range(1,n+1): # 1,2,3,...,n
        yield i # returns i and pauses until called

s = rangefunc(3)

print(next(s))
print(next(s))
print(next(s))
# StopIteration error is raised while printing fifth time, uncomment below line to see
# print(next(s)) 