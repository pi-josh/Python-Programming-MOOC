"""
Programming exercise:
Absolute value

Please write a program which asks the user for an integer number.
If the number is less than zero, the program should print out
the number multiplied by -1. Otherwise the program prints out
the number as is. Please have a look at the examples of expected
behavior below.

Sample output
Please type in a number: -7
The absolute value of this number is 7

Sample output
Please type in a number: 1
The absolute value of this number is 1

Sample output
Please type in a number: -99
The absolute value of this number is 99
"""
# Write your solution here
num = int(input("Please type in a number: "))

if num >= 0:
    print(f"The absolute value of this number is {num}")
    
if num < 0:
    print(f"The absolute value of this number is {num * -1}")