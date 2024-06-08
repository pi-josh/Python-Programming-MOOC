# write your solution here
text = input("Write text: ")
words = text.split()

wordlist = []
with open("wordlist.txt") as file:
    for word in file:
        word = word.replace("\n", "")
        wordlist.append(word)

for word in words:
    if word.lower() not in wordlist:
        print(f"*{word}*", end=" ")
    else:
        print(word, end=" ")
        