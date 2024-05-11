# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string: str) -> bool:
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    return False

def main():
    while True:
        string = input("Please type in a palindrome: ")
        
        if palindromes(string):
            break
        else:
            print("that wasn't a palindrome")
    print(f"{string} is a palindrome!")
    
main()