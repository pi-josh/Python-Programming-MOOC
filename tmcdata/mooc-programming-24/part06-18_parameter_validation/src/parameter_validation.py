# Write your solution here
def new_person(name: str, age: int) -> tuple:
    length = len(name)
    words = name.strip().split()
    if not (length > 0 and length <= 40) or \
            len(words) < 2 or \
        not (age >= 0 and age <= 150):
            raise ValueError
    
    return (name, age)


if __name__ == "__main__":
    person = new_person('Andrew', 32)