f1 = open('scource.txt','r+')

content = f1.readlines() # reads each line one by one and appends ecah line to a list

f2 = open('destination.txt','w+')


for lines in content:
    f2.write(lines)

""" After writing line by line the file pointer will be in the last line of destination .txt """
# bring it back to the first line using seek


f2.seek(0,0)
print(f2.read())

f1.close()
f2.close()