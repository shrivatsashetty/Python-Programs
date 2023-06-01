# comparing time taken by while and for loop using time module
import time

program_start=time.time()

while_start=time.time()
i=0
while (i<=100000000): # output will take some time wait patiently
    # print(i)
    i+=1
while_end=time.time()
print("while took",while_end-while_start)

for_start=time.time()
for i in range(100000000): 
    # print(i)
    continue
for_end=time.time()

print("for took: ",for_end-for_start)
print()



