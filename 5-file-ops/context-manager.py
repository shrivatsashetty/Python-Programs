# Specify the file path

# file_path = "path/to/your/file.txt"

# Open the file using 'with' and 'as'

try:
    with open("fruits.txt", 'r') as file:
        # Perform operations on the file
        content = file.read()
        print(content)

except Exception as e:
    print("An Error occoured:",e)
