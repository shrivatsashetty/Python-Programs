# Sort caharacters of strings
test="wer@rv!$%12"
for i in test:
    if(i in '1234567890'):
        #to check special char using in function
        print(f"{i} is a integer")
    elif i in '!@#$%^&*()_+-=><?.,":][]}{':
        print(i,"is special character")
    else:
        print(i , "is a charcter")