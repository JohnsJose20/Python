'''
Authore: Johns Jose
Date: 25-10-2024
Description:
'''

num =int(input("Enter a number:"))
Input_num=num
sum_of_digits=0
while num>0:
    remainder = num%10
    power=remainder
    sum_of_digits=sum_of_digits+power**3
    num = num//10
if sum_of_digits==Input_num:
    print("The Give number is amsrtong")