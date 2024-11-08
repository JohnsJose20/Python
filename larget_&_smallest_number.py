limit=int(input("Enter the limit:"))
num=int(input("Enter number:"))
small = num
big = num
while(limit>1):
    num = int(input("Enter number:"))
    if num>big:
        big=num
    if num<small:
        small=num
    limit=limit-1
print("the largest number is", big)
print("the smallest number is",small)
