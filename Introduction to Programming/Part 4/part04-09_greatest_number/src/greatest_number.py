# Write your solution here
def greatest_number(num1, num2, num3):
    max = num1
    if max < num2:
        max = num2
    if max < num3:
        max = num3
    return max

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)