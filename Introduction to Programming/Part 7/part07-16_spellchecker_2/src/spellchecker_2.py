# Write your solution here
from difflib import get_close_matches

# prompt for text to check
text = input("write text: ").strip()
words = text.split(" ")

# store list of words from the given file
word_list = []
with open("wordlist.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        word_list.append(line)

# print misspelled words and store in a dict
misspelled_word = {}
for word in words:
    if word.lower() not in word_list:
        print(f"*{word}*", end=" ")
        if word not in misspelled_word:
            misspelled_word[word] = []
    else:
        print(word, end=" ")

# check for word suggestions
for word in misspelled_word:
    misspelled_word[word] = get_close_matches(word, word_list)

# display word suggestions for each misspelled words
print("\nsuggestions:")
for word, suggestions in misspelled_word.items():
    print(f"{word}: {", ".join(suggestions)}")