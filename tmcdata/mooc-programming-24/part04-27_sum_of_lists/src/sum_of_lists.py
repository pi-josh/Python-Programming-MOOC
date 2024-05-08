# Write your solution here
def list_sum(list1: list, list2: list) -> list:
    new_list = []
    for i in range(len(list1)):
        sum = list1[i] + list2[i]
        new_list.append(sum)
    return new_list