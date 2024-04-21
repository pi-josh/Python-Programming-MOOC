"""
Programming exercise:
Seconds in a day

Please write a program which asks the user for a number of days.
The program then prints out the number of seconds in the amount
of days given.

The program should function as follows:
Sample output:
How many days? 1
Seconds in that many days: 86400

Another example:
Sample output:
How many days? 7
Seconds in that many days: 604800
"""
# Write your solution here
days = int(input("How many days? "))

seconds = days * 24 * 60 * 60   # There are 24 hours in a day, 60 minutes in one hour, and 60 seconds in one minute
print(f"Seconds in that many days: {seconds}")