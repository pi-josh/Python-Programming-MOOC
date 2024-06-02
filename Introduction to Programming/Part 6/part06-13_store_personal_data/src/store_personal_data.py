# Write your solution here
def store_personal_data(person: tuple):
    record = f"{person[0]};{person[1]};{person[2]}\n"
    file = open("people.csv", "a")
    file.write(record)
    file.close()


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))