from string import ascii_letters, punctuation

# Write your solution here
def separate_characters(my_string: str) -> tuple:
    ascii = ""
    punctuations = ""
    others = ""
    for character in my_string:
        if character in ascii_letters:
            ascii += character
        elif character in punctuation:
            punctuations += character
        else:
            others += character
            
    return (ascii, punctuations, others)


if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])