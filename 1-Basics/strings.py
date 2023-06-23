# String operations
name="Shrivatsa A Shetty"
#Upper & lower case operation
print("the name is "+name.upper()) #name string with an operation
print("in small case "+name.lower())
#finding a substring
print(name.find(' ')) # finding index of space character
print(name.find('Shetty'))
print(name.find('A'))
print(name.find('_'))
print(name.find('f')) # f does not occur in my name so -1 is returned
a=name.find(' ')  #name.find returns a number which can be stored in a variable
b=name.find('A')
print("a+b is",a+b)
print("My nickname is "+name.replace("Shrivatsa A Shetty","Siri"))
print("also call me "+name.replace("A Shetty","Shetre "))
print("or "+name.replace("A","kadoor "))
print("im a bunt and thats","Shetty" in name) #finding if a  substring exist in a string
print("originally entered as "+name)
