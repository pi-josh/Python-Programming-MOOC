# Write your solution here
phone_book = {}

while True:
    command = int(input("command(1 search, 2 add, 3 quit): "))
    match command:
        case 1:
            name = input("name: ")
            if name in phone_book.keys():
                print(phone_book[name])
            else:
                print("no number")
        case 2:
            name = input("name: ")
            number = input("number: ")
            phone_book[name] = number
            print("ok!")
        case 3:
            print("quitting...")
            break