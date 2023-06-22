lst=[1,2,3,4,5,6]

it=lst.__iter__() # or it=iter(lst) 

# uncomment any one of the following block and see results

"""Block 1"""
# print(next(it))
# print(it.__next__())

"""Block 2"""
try:
    while True:
        print(next(it))
except Exception as e:
    print(e)
    print("iterable ends")

'''Block 3'''  
# for i in range(len(lst)):
#     print(next(it))
