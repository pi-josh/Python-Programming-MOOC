"""
Programming exercise:
First letters of words

Please write a program which asks the user to type in a sentence.
The program then prints out the first letter of each word in the
sentence, each letter on a separate line.

An example of expected behaviour:

Sample output
Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w
"""
sentence = " " + input("Please type in a sentence: ")   # Adding a space
                                # at the front to make the handling easier
index = 1
while index < len(sentence):
    if sentence[index-1] == ' ' and sentence[index] != ' ':
        print(sentence[index])
    index += 1


"""
# For optimization
sentence = input("Please type in a sentence: ").split()

for word in sentence:
    print(word[0])"""