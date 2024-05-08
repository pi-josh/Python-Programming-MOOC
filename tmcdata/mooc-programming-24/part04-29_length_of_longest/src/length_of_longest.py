# Write your solution here
def length_of_longest(my_list: list) -> int:
    longest = len(my_list[0])
    for word in my_list:
        length = len(word)
        if length > longest:
            longest = length
    return longest