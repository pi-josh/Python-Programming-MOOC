# write your solution here
def read_fruits():
    """Returns a dictionary of fruits with its price from the given csv file"""
    fruits = {}
    with open("fruits.csv") as f:
        for line in f:
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruits[fruit] = price
    
    return fruits


if __name__ == "__main__":
    fruits = read_fruits()
    for fruit, price in fruits.items():
        print(f"{fruit}: {price}")