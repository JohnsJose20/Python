'''
Authore: Johns Jose
Date: 25-10-2024
Description: Write a Python program to get the sum of the numbers
'''
num =int(input("Enter a number:"))
sum_of_digits=0
while num>0:
    remainder = num%10
    sum_of_digits = sum_of_digits+remainder
    num = num//10
print("Sum of  Digits of the given number: ",sum_of_digits)