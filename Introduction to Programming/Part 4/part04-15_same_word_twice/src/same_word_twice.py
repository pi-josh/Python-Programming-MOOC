# Write your solution here
words = []
word_count = 0

while True:
    word = input("Word: ")
    
    if word in words:
        break
    else:
        words.append(word)
        word_count += 1
print(f"You typed in {word_count} different words")