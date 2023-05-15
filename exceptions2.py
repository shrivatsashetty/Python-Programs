try:
    l=[0,1,2,3]
    i=input("Enter an index:")
    try:
        print(f"The item at the index {i} is",l[int(i)])
    except Exception as mistake:
        print("The error is:",mistake)
        print("Index can only be an integer")
# the control of the program never comes to below except block since the exception will be handled above itself
except:
    print("Entered index is out of range")

print("=====THE END=====")

