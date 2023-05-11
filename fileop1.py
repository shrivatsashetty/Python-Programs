try:
    f1=open("mssg.txt","r")
    content=f1.read()
    print(content)

except FileNotFoundError:
    print("File not found")

except:
    print("Some error occoured")

finally:
    f1.close()