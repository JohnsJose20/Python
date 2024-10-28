'''
Authore: Johns Jose
Date: 28-10-2024
Description: Write a menu-driven Python program that allows users to convert temperatures
between Celsius and Fahrenheit.
The program should repeatedly display a menu with three options:
    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program'''

while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    option =int(input("Enter your option:"))
    if option==1:
        Temp_in_C=int(input("Enter a temperature in Celsius: "))
        Fahrenheit = (9 / 5 * Temp_in_C) + 32
        print(f"{Fahrenheit} Fahrenheit")
    elif option==2:
        Temp_in_F=int(input("Enter a temperature in Fahrenheit: "))
        Celsius = 5 / 9 * (Temp_in_F - 32)
        print(f"{Celsius} Celsius")
    elif option==3:
        break
    else:
        print("Invalid Entry")




