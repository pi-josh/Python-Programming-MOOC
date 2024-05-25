# Write your solution here
def no_shouting(my_list: list) -> list:
    # return [string for string in my_list if not string.isupper()] # using list comprehension
    pruned_list = []
    for string in my_list:
        if not string.isupper():
            pruned_list.append(string)
    return pruned_list


def main():
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)


if __name__ == "__main__":
    main()