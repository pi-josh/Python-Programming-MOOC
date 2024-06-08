# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
    word_list = []
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning):
                word_list.append(line)
    
    return sample(word_list, n)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)