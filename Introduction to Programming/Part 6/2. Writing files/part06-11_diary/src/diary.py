# Write your solution here
FILE_NAME = "diary.txt"

def add_entry():
    entry = input("Diary entry: ")
    with open(FILE_NAME, "a") as file:
        file.write(entry+"\n")
    print("Diary saved\n")


def read_entries():
    print("Entries:")
    with open(FILE_NAME) as file:
        for entry in file:
            entry = entry.strip()
            print(entry)


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")
    
    match function:
        case '0':
            print("Bye now!\n")
            break
        case '1':
            add_entry()
        case '2':
            read_entries()