"""
Programming exercise:
A square of hashes

Please write a function named hash_square(length), which takes
an integer argument. The function prints out a square of hash
characters, and the argument specifies the length of the side of the
square.

hash_square(3)
print()
hash_square(5)
Sample output
###
###
###

#####
#####
#####
#####
#####
"""
# Write your solution here
def hash_square(length):
    for _ in range(length):
        for _ in range(length):
            print("#", end="")
        print()

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)