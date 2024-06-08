# Write your solution here
from datetime import datetime

new_millennium = datetime(1999, 12, 31)

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthdate = datetime(year, month, day)

if birthdate <= new_millennium:
    difference = new_millennium - birthdate
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")
    
