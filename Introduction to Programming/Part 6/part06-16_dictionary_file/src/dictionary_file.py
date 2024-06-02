# Write your solution here
filename = "dictionary.txt"
dictionary = {}

with open(filename) as file:
        for line in file:
            finnish, english = line.strip().split(";")
            dictionary[finnish] = english
            
            
def add_word():
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    dictionary[finnish] = english
    print("Dictionary entry added")
    
    with open(filename, "w") as file:
        for finnish, english in dictionary.items():
            line = f"{finnish};{english}\n"
            file.write(line)


def search_word():
    search_term = input("Search term: ")
    
    for finnish, english in dictionary.items():
        line = f"{finnish} - {english}"
        if search_term in line:
            print(line)


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    
    match function:
        case '1':
            add_word()
        case '2':
            search_word()
        case '3':
            print("Bye!")
            break