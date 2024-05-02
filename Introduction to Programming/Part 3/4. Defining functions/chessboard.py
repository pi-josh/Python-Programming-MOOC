"""
Programming exercise:
Chessboard

Please write a function named chessboard, which prints out a
chessboard made out of ones and zeroes. The function takes an
integer argument, which specifies the length of the side of the
board. See the examples below for details:

chessboard(3)
print()
chessboard(6)

Sample output
101
010
101

101010
010101
101010
010101
101010
010101
"""
# Write your solution here
def chessboard(length):
    for i in range(length):
        for j in range(length):
            if (i + j) % 2 == 0:
                print(1, end="")
            else:
                print(0, end="") 
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(3)
