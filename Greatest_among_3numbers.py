'''
Authore: Johns Jose
Date: 25-10-2024
Description: Write a Python program to find the largest of three numbers.
The program should take three numbers as input from the user and determine which one is the largest.
Use conditional statements to compare the numbers.
'''

Num_1=int(input("Enter first number:"))
Num_2=int(input("Enter second number:"))
Num_3=int(input("Enter third number:"))
if Num_1>Num_2 and Num_1>Num_3:
    print(Num_1,"is greater than the other three number")
elif Num_2>Num_3:
    print(Num_2,"is greater than the other three number")
else:
    print(Num_3, "is greater than the other three number")
