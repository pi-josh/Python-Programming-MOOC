# Write your solution here
def histogram(string: str) -> dict:
    my_dict = {}
    for character in string:
        if character not in my_dict:
            my_dict[character] = ""
        my_dict[character] += '*'
        
    for key, value in my_dict.items():
        print(key, end=" ")
        print(value)
    print()

if __name__ == "__main__":
    histogram("abba")
    histogram("statistically")