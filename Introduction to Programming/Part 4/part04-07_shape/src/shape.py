# Copy here code of line function from previous exercise and use it in your solution
def line(length, string):
    for _ in range(length):
        if string == '':
            print('*', end="")
        else:
            print(string[0], end="")
    print()
    
def shape(width, roof, height, base):
    for i in range(1, width+1):
        line(i, roof)
    
    for _ in range(height):
        line(width, base)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")