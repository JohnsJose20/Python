'''
Authore: Johns Jose
Date: 30-11-2024
Description:'''

def factorial(num):
    if num>=0:
        if num == 0:
            return 1
        else:
            return(num*factorial(num-1))
number=int(input("Enter a number:"))
custom=factorial(number)
print(f"The factorial of the given number is {custom}")