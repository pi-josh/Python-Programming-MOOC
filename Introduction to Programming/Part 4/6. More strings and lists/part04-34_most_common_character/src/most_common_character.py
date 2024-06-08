# Write your solution here
def most_common_character(string: str) -> str:
    most_common = string[0]
    for character in string:
        if string.count(character) > string.count(most_common):
            most_common = character
    return most_common

def main():
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

if __name__ == "__main__":
    main()