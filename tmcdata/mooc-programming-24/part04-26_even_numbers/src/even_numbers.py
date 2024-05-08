# Write your solution here
def even_numbers(my_list: list) -> list:
    even_list = []
    for num in my_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list