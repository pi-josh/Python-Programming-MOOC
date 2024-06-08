# Write your solution h
def change_case(orig_string: str) -> str:
    return orig_string.swapcase()


def split_in_half(orig_string: str) -> str:
    length = len(orig_string)
    half = length // 2
    first_half, second_half = orig_string[:half], orig_string[half:]
    return first_half, second_half


def remove_special_characters(orig_string: str) -> str:
    return "".join([character for character in orig_string if character.isalnum() or character.isspace()])


if __name__ == "__main__":
    print(change_case("hEllO"))
    print(split_in_half("hello"))
    print(split_in_half("hellos"))
    print(remove_special_characters("ed1§wo r!!!??s8876"))