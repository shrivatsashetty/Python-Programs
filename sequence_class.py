class Sequence:
    def fibbonacci(self,n = 0):
        # n = int(input("How many terms u need:")) 
        a,b = 0,1
        for i in range(n):
            yield a
            a,b = b,b+a


