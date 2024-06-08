# Write your solution here
def everything_reversed(my_list: list) -> list:
    reversed_strings = []
    for string in my_list:
        reversed_strings.append(string[::-1])
    return reversed_strings[::-1]

def main():
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    
if __name__ == "__main__":
    main()