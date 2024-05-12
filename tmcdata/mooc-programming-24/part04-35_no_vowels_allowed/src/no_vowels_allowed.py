# Write your solution here
def no_vowels(my_string: str) -> str:
    vowels = "aeiou"
    new_string = ""
    for character in my_string:
        if not character in vowels:
            new_string += character
    return new_string


def main():
    my_string = "this is an example"
    print(no_vowels(my_string))


if __name__ == "__main__":
    main()