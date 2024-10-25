'''
Authore: Johns Jose
Date: 25-10-2024
Description: Write a Python program to convert temperature values back
 and forth between Celsius and Fahrenheit
'''

Temp=int(input("Enter temperature:"))
C_or_F= input("Is this in (C)elsius or (F)ahrenheit?")
if C_or_F=="C":
    Fahrenheit=(9/5*Temp)+32
    print(Temp," Celsius is ",Fahrenheit,"Fahrenheit")
elif C_or_F=="F":
    Celsius=5/9*(Temp-32)
    print(Temp,"Fahrenheit is",Celsius,"Celsius")
else:
    print("invalid temperature code")