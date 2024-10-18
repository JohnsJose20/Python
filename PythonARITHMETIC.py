'''
Authore: Johns Jose
Date: 18-10-2024
Description: A Python program that demonstrates the usage of arithmetic, comparison, and logical operators. Perform a few operations and print the results.
Instructions:
    Perform addition and division using two integers (a = 10, b = 5).
    Compare the two integers using the greater-than (>) and equality (==) operators.
    Use logical operators (and, or) to check conditions.
    Display the results of all the operations.
'''

number_1 = int(input("Enter the first number:"))
number_2 = int(input("Enter the second number"))
print("Sum=",number_1+number_2,",Division=",number_1/number_2)
print("Is number_1 greater than number_2?:",number_1>number_2)
print("Are number_1 and number_2 equal?:",number_1==number_2)
print("Logical AND:",number_1>0 and number_2>0)
print("Logical OR:",number_1>0 or number_2>number_1)
