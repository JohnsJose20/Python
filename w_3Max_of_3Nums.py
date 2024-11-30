'''
Authore: Johns Jose
Date: 30-11-2024
Description:'''

def max_of_3_nums(num1,num2,num3):
    nums=[num1,num2,num3]
    nums.sort()
    return nums[2]
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
custom = max_of_3_nums(num1, num2,num3)
print(f"The greatest number is {custom}")