"""
Programming exercise:
The next leap year

Please write a program which asks the user for a year, and prints
out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the
program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028
"""
# Write your solution here
year = int(input("Year: "))

print(f"The next leap year after {year} is ", end="")
while True:
    year += 1
    if year % 4 != 0:
        continue
    elif year % 100 != 0:
        break
    elif year % 400 != 0:
        continue
    else:
        break
print(year)