"""
Programming exercise:
End to beginning

Please write a program which asks the user for a string. The
program then prints out the input string in reversed order, from
end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h
"""
# Write your solution here
string = input("Please type in a string: ")
strlen = len(string)

while strlen > 0:
    print(string[strlen - 1])
    strlen -= 1
