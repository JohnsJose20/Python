'''
Authore: Johns Jose
Date: 29-11-2024
Description: Program to check whether the given
number is a valid mobile number or not using functions.
'''
def valid_number (num):
    if len(num)==10 and (num[0]=="7") or (num[0]=="9") or (num[0]=="8"):
        return True
    return False
mobile_num=input("Enter the Mobile number:")
if valid_number(mobile_num):
    print(f"The Given Mobile number {mobile_num} is valid")
else:
    print(f"The Given Mobile number {mobile_num} is not valid")


