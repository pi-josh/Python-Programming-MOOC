"""
Programming exercise:
A word squared

Please write a function named squared, which takes a string
argument and an integer argument, and prints out a square of
characters as specified by the examples below.

squared("ab", 3)
print()
squared("aybabtu", 5)
Sample output
aba
bab
aba

aybab
tuayb
abtua
ybabt
uayba
"""
# Write your solution here
def squared(text, length):
    # I'll be back
    new_text = ""
    while len(new_text) < length ** 2:
        new_text += text
    
    new_text = new_text[:length**2]
    
    for i in range(len(new_text)):
        print(new_text[i], end="")
        if (i + 1) % length == 0:
            print()

# Driver code
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
    