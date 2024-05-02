"""
Programming exercise:
A rectangle of hashes

Please modify the previous program so that it also asks for the
height, and prints out a rectangle of hash characters accordingly.

Sample output
Width: 10
Height: 3
##########
##########
##########
"""
# Write your solution here
width = int(input("Width: "))
height = int(input("Height: "))

while height > 0:
    print("#" * width)
    height -= 1