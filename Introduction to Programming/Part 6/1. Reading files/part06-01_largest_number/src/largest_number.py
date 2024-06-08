# write your solution here
def largest() -> int:
    """Returns the largest number in the given text file"""
    with open("numbers.txt") as f:
        numbers = []
        for number in f:
            numbers.append(int(number))
        
        return max(numbers)


if __name__ == "__main__":
    largest_num = largest()
    print(f"Largest number in the text file: {largest_num}")