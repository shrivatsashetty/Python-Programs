set1={100,108,"Cricket","Football",'#','@'}
print("set 1 is:",set1)
set2={"hello",7,"bye",'a','b'}
print("set 2 is:",set2)
empty_set=set()
print("an empty set looks like",empty_set)
print("data type of empty_set is",type(empty_set))
# 1.addition of element
set1.add(3)
print("updated set:",set1)
# 2.updating of the set
set1.update(set2)
print("updated set1",set1)
# 3.Remove an element
set1.discard("bye")
print("updated set1",set1)
# 4.no of elements
print("no of elements in set1 is",len(set1))
set3={"Cricket","hello",100,3,"yeah","hi",'^',123}
print("set1:",set1)
print("set3:",set3)
# 5.union operation
print("union of sets",set1|set3)
# 6.intersection
print("common elements of sets",set1&set3)
# 7.Set Difference
print("difference of sets",set1-set3)
# 8.symmetric difference
print("symmetric diff of sets",set1^set3)
# 9.Checking equality
if set1==set3:
    print("The sets 1 & 3 are equal")
else:
    print("set 1 and 3 are not equal")
subset={3,100,7}
if subset.issubset(set1):
    print(subset,"is subset of",set1)
else:
    print(subset,"not a subset of",set1)
if set1.issuperset(subset):
    print("set 1 is dad and ",subset,"is son")
else:
    print("not a superset")
