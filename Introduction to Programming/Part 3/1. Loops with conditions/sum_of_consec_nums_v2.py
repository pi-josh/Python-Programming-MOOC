"""
Programming exercise:
The sum of consecutive numbers, version 2

Please write a new version of the program in the previous exercise.
In addition to the result it should also print out the calculation
performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10

Sample output
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

You may assume the number typed in by the user is always equal to
2 or higher.
"""
# Write your solution here
limit = int(input("Limit: "))
number = 1
sum = 1
format = "The consecutive sum: 1"
while sum < limit:
    number += 1
    sum += number
    format += f" + {number}"
format += f" = {sum}"
print(format)