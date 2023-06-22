class MyList:
    def __init__(self,*args):
        self.data=list(args)

    def __getitem__(self,index):
        return self.data[index]
    
    def __setitem__(self,index,value):
        self.data[index] = value

    def __str__(self):
        return f"List: {self.data}"
odds = MyList(1,3,5,7,9)
evens = MyList(2,4,6,8,10)

print(odds[4])
print(evens)
