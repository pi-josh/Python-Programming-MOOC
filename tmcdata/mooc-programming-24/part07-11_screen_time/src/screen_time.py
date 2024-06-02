# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
start_date = input("Starting date: ")
days = int(input("How many days: "))

# partition the starting date
day, month, year = list(map(int, start_date.strip().split(".")))

# parse the datetimes
start_datetime = datetime.strptime(start_date, "%d.%m.%Y")
end_datetime = start_datetime + timedelta(days=days-1)

# prompt for the screen times
screen_times = []
current_datetime = start_datetime

print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(days):
    screen_time = input(f"Screen time {current_datetime.strftime("%d.%m.%Y")}: ").strip()
    minutes = list(map(int, screen_time.split(" ")))
    screen_times.append(minutes)
    current_datetime += timedelta(days=1)

# calculate total and average minutes
total = 0
for minutes in screen_times:
    for minute in minutes:
        if minute != 0:
            total += minute
average = total / days

# write infos to the given filename
with open(filename, "w") as file:
    file.write(f"Time period: {start_datetime.strftime("%d.%m.%Y")}-{end_datetime.strftime("%d.%m.%Y")}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average}\n")
    
    current_datetime = start_datetime
    for i in range(days):
        file.write(f"{current_datetime.strftime("%d.%m.%Y")}: {'/'.join(map(str, screen_times[i]))}\n")
        current_datetime += timedelta(days=1)
    print(f"Date stored in file {filename}")