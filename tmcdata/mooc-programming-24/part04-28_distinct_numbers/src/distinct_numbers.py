# Write your solution here
def distinct_numbers(my_list: list) -> list:
    distinct_list = []
    for num in sorted(my_list):
        if not num in distinct_list:
            distinct_list.append(num)
    return distinct_list