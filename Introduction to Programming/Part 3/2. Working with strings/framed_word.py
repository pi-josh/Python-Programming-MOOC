"""
Programming exercise:
A framed word

Please write a program which asks the user for a string and then
prints out a frame of * characters with the word in the centre. The
width of the frame should be 30 characters. You may assume the
input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out
the word in either of the two possible centre locations.

Sample output
Word: testing

******************************
*          testing           *
******************************
Sample output
Word: python

******************************
*           python           *
******************************
"""
# Write your solution here
word = input("Word: ")
print("*" * 30)
if len(word) % 2 == 0:
    print("*" + (" " * ((28 - len(word))//2)) + word + " " * ((28 - len(word))//2) + "*")
else:
    print("*" + (" " * ((28 - len(word))//2)) + word + " " * ((28 - len(word))//2 + 1) + "*")
print("*" * 30)

"""# For readability
word = input("Word: ")
print("*" * 30)

spaces_at_start = (28 - len(word)) // 2
spaces_at_end = (28 - len(word)) // 2

if len(word) % 2 != 0:
    spaces_at_end += 1
print("*" + " " * spaces_at_start + word + " " *  spaces_at_end + "*")
print("*" * 30)"""