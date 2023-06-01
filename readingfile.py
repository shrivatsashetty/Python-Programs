try:
    fptr=open('testfile.txt','r') # fptr is a file pointer object
    print(fptr)
    content=fptr.read()
    print(content)
    fptr.close()
except Exception as e:
    print(e)

print("Program completed")