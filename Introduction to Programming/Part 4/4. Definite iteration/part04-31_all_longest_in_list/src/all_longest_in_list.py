# Write your solution here
def all_the_longest(my_list: list) -> list:
    longest_length = len(my_list[0])
    for word in my_list:
        length = len(word)
        if length > longest_length:
            longest_length = length
    
    longest_list = []
    for word in my_list:
        if len(word) == longest_length:
            longest_list.append(word)
    return longest_list