# Write your solution here
from string import ascii_lowercase, digits
from random import sample


def generate_strong_password(length: int, has_number: bool, has_punctuation: bool) -> str:
    while True:
        password = ascii_lowercase
        punctuation = "!?=+-()#"
        if has_number:
            password += digits
        if has_punctuation:
            password += punctuation
        
        password = sample(password, length)
        contains_num = False
        contains_punctuation = False
        contains_lowercase = False
        
        if has_number:
            for character in password:
                if character in digits:
                    contains_num = True
                if character in ascii_lowercase:
                    contains_lowercase = True
        
        if has_punctuation:
            for character in password:
                if character in punctuation:
                    contains_punctuation = True
                if character in ascii_lowercase:
                    contains_lowercase = True
        
        password = "".join(password)
        if has_number and has_punctuation and contains_num and contains_lowercase and contains_punctuation:
            return password
        elif has_number and not has_punctuation and contains_num and contains_lowercase:
            return password
        elif has_punctuation and not has_number and contains_punctuation and contains_lowercase:
            return password
        elif not has_number and not has_punctuation:
            return password
        else:
            continue




if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, True, True))