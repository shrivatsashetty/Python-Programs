from sequence_class import Sequence

obj = Sequence()

n = int(input("Enter no of terms:"))
buffer = obj.fibbonacci(n)
for i in  range(n):
    print(next(buffer))