# Write your solution here
from string import ascii_lowercase
from random import sample

def generate_password(length: int) -> str:
    password = sample(ascii_lowercase, length)
    return ''.join(password)


if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))