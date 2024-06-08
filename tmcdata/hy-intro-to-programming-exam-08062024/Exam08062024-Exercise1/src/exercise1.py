# Write your solution to exercise 1 here
string_count = 0
longest_string = ""
characters = {}

while True:
    string = input("Type in a string: ")
    if not string:
        break
    string_count += 1
    
    # check if current string is the longer
    if len(string) > len(longest_string):
        longest_string = string
    
    # store each character and its count
    for character in string:
        if character not in characters:
            characters[character] = 0
        characters[character] += 1

# check the character with the most count
highest_count = 0
most_common = ""
for character in characters:
    if characters[character] > highest_count:
        highest_count = characters[character]
        most_common = character

# display outputs
print(f"Total number of strings: {string_count}")
print(f"The length of the longest string: {longest_string}")
print(f"The most common character in strings: {most_common}")