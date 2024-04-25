"""
Programming exercise:
Typecasting

When programming in Python, often we need to change the data
type of a value. For example, a floating point number can be
converted into an integer with the function int:


temperature = float(input("Please type in a temperature: "))

print("The temperature is", temperature)

print("...and rounded down it is", int(temperature))

Sample output
Please type in a temperature: 5.15
The temperature is 5.15
...and rounded down it is 5

Notice the function always rounds down, and not according to the
rounding rules in mathematics. This is an example of a floor
function.

Sample output
Please type in a temperature: 8.99
The temperature is 8.99
...and rounded down it is 8

Please write a program which asks the user for a floating point
number and then prints out the integer part and the decimal part
separately. Use the Python int function.

You can assume the number given by the user is always greater
than zero.

An example of expected behavior:

Sample output
Please type in a number: 1.34
Integer part: 1
Decimal part: 0.34
"""
# Write your solution here
num = float(input("Please type in a number: "))
integer_part = int(num)
decimal_part = num - integer_part

print(f"Integer part: {integer_part}")
print(f"Decimal part: {decimal_part}")