"""
Programming exercise:
Alphabetically in the middle

Please write a program which asks the user for three letters. The
program should then print out whichever of the three letters would
be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all
lowercase.

Some examples of expected behaviour:

Sample output
1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output
1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
"""
# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first < second < third or first > second > third:
    print(f"The letter in the middle is {second}")
elif first < third < second or first > third > second:
    print(f"The letter in the middle is {third}")
else:
    print(f"The letter in the middle is {first}")