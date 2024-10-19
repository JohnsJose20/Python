'''
Authore: Johns Jose
Date: 19-10-2024
Create, concatenate, and print a string and
access a sub-string from a given string.
'''

First_name=input("Enter Your First Name: ")
Last_name=input("Enter Your Last Name: ")
Name=First_name+" "+Last_name
print(Name)
First_name_length=len(First_name)
print(First_name_length)
Extracted_first_name=Name[:First_name_length]
print(Extracted_first_name)
Extracted_last_name=Name[First_name_length+1:]
print(Extracted_last_name)