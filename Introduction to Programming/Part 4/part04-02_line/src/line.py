# Write your solution here
def line(length, string):
    for _ in range(length):
        if string == '':
            print('*', end="")
        else:
            print(string[0], end="")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")