"""
Programming exercise:
Food expenditure

Please write a program which estimates a user's typical food
expenditure.

The program asks the user how many times a week they eat at the
student cafeteria. Then it asks for the price of a typical student
lunch, and for money spent on groceries during the week.

Based on this information the program calculates the user's typical
food expenditure both weekly and daily.

The program should function as follows:

Sample output
How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""
# Write your solution here
times_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_spend = float(input("How much money do you spend on groceries in a week? "))

daily = (lunch_price * times_per_week + grocery_spend) / 7 # There are 7 days a week
weekly = grocery_spend + lunch_price * times_per_week

print("Average food experience:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")