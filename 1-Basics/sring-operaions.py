# scentence1="I love programing"
# # acessing elements using index
# print(scentence1[-4]) # return 4th item from last
# #slicing
# print(scentence1[2:4])#slicing 
# # in slicing the element at the end indedx is not itself included
# print(scentence1)
# lines="""Two roads diverged in a yellow wood
# and i choose the one less travelled by"""
# # print length of a string
# print(len(lines))
# # comparing strings
# str1=input("Write a line:")
# str2=input("write another line:")
# if (str1==str2):
#     print("The two strings are same")
# else:
#     print("The string are not the same")
# #concatenation
# scentence1="we love programing"
# scentence2="we  like maths"
# print(scentence1+" and "+scentence2)
# # check membership
# print(lines)
# search_string=input("Enter a string to search:")
# str="APNA COLLEGE"
# #length test
# print(len(str))
# #slicing
# print(str[:])# APNA COLLEGE
# print(str[3:])# A COLLEGE
# print(str[:6])# APNA C
# # membership test
# print("APNA" in str)# True
str="APNA COLLEGE"

#length test
print(len(str))

#indexing
print(str[-3])# E

#slicing
print(str[:])# APNA COLLEGE
print(str[3:])# A COLLEGE
print(str[:6])# APNA C
print(str[-1:-12:-5])

# membership test
print("APNA" in str)# True
print("APNA" not in str)# False

#string repeat
print(3*"COLLEGE")# COLLEGECOLLEGECOLLEGE
print(2*str)# APNA COLLEGEAPNA COLLEGE

#concatenation
print("Hi"+" "+"Hello"+" "+"Namaste")# Hi Hello Namaste

#find 
print(str.find("N"))# 2 ,returns index of search string
print(str.find("COLL"))# 5 
print(str.find("COLG"))# -1 ,indicating that the search string is not there

#STRING METHODS

#capitalize first letter of each word








