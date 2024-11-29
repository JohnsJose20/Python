'''
Authore: Johns Jose
Date: 29-11-2024
Description:Program to find the factorial of a number using Recursion.
'''
def right_triangle_ro_not (side):
    side.sort()
    if side[2]**2==side[0]**2 + side[1]**2:
        return True
    return False
side = []
side.append(int(input("Enter the first length:")))
side.append(int(input("Enter the first length:")))
side.append(int(input("Enter the first length:")))
if right_triangle_ro_not(side):
    print("The given side are a part of right triangle")
else:
    print("The Given side are not a part of right triangle")