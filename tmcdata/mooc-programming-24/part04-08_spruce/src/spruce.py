# Write your solution here
def spruce(height):
    print("a spruce!")
    for i in range(1, height+1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    print(" " * (height - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)