# Write your solution here
def read_input(prompt: str, start: int, end: int) -> int:
    while True:
        try:
            number = int(input(prompt))
            if number in range(start, end+1):
                return number
        except ValueError:
            pass
        
        print(f"You must type in an integer between {start} and {end}")
        

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)