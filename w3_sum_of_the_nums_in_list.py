'''
Authore: Johns Jose
Date: 30-11-2024
Description:'''

def addition_of_list(list):
    sum = 0
    for i in list:
        sum = sum+i
    print(sum)
list = []
nums= int(input("Enter the number of elements:"))

for i in range (nums):
    num=int(input("Enter the number:"))
    list.append(num)
print(list)
addition_of_list(list)