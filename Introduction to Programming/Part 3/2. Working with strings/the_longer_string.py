"""
Programming exercise:
The longer string

Please write a program which asks the user for two strings and then
prints out whichever is the longer of the two - that is, whichever has
the more characters. If the strings are of equal length, the program
should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long
"""
# Write your solution here
string1 = input("Please type in string 1: ")
string2 = input("Please type in string 2: ")

if len(string1) > len(string2):
    print(string1 + " is longer")
elif len(string1) < len(string2):
    print(string2 + " is longer")
else:
    print("The strings are equally long")