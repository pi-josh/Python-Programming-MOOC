"""
Programming exercise:
Does it contain vowels

Please write a program which asks the user to input a string. The
program then prints out different messages if the string contains
any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look
at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found
"""
# Write your solution here
string = input("Please type in a string: ")

print("a found" if 'a' in string else "a not found")
print("e found" if 'e' in string else "e not found")
print("o found" if 'o' in string else "o not found")