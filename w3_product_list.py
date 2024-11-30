'''
Authore: Johns Jose
Date: 30-11-2024
Description:'''

def product_of_list(list):
    product = 1
    for i in list:
        product = product*i
    print(product)
list = []
nums= int(input("Enter the number of elements:"))

for i in range (nums):
    num=int(input("Enter the number:"))
    list.append(num)
print(list)
product_of_list(list)