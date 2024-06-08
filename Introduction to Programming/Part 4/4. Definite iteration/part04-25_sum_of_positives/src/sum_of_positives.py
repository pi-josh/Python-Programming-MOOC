# Write your solution here
def sum_of_positives(my_list: list) -> int:
    sum = 0
    for num in my_list:
        if num > 0:
            sum += num
    return sum