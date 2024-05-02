"""
Programming exercise:
Substrings, part 1

Please write a program which asks the user to type in a string. The
program then prints out all the substrings which begin with the first
character, from the shortest to the longest. Have a look at the
example below.

Sample output
Please type in a string: test
t
te
tes
test
"""
# Write your solution here
string = input("Please type in a string: ")
last = 1
while last <= len(string):
    print(string[:last])
    last += 1