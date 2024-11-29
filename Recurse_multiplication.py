'''
Authore: Johns Jose
Date: 29-11-2024
Description: Recursive function to multiply two positive numbers
'''

def multiplication(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1 + multiplication(num1,num2-1)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
custom=multiplication(num1,num2)
print(f"The product of {num1} and {num2} is {custom}")