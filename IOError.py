try:
    fptr=open("no_file.txt","r")
    file_content=fptr.read()
    print(file_content)
except IOError:
    print("No such file")

finally:
    fptr.close()


print(f"outside try & except:{1}/{2}={1/2}")