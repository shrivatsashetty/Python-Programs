f=open('myfile2.txt','w')
content=f.write(""" hello this is written using write mode""")
# change this text every time u run the program and see the difference
print(content)
f.close() # after opening always close a file


