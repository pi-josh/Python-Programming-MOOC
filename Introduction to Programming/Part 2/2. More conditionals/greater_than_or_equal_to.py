"""
Programming exercise:
Greater than or equal to

Please write a program which asks for two integer numbers. The
program should then print out whichever is greater. If the numbers
are equal, the program should print a different message.

Some examples of expected behaviour:

Sample output
Please type in the first number: 5
Please type in another number: 3
The greater number was: 5

Sample output
Please type in the first number:: 5
Please type in another number: 8
The greater number was: 8

Sample output
Please type in the first number: 5
Please type in another number: 5
The numbers are equal!
"""
# Write your solution here
num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in the second number: "))

if num1 > num2:
    print("The greater number was:", num1)
elif num1 < num2:
    print("The greater number was:", num2)
else:
    print("The numbers are equal!")
