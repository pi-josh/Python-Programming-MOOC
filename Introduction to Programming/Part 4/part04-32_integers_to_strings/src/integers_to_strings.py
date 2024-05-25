# Write your solution here
def formatted(my_list: list) -> list:
    new_list = []
    
    for num in my_list:
        new_list.append(f"{num:.2f}")
    return new_list

def main():
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
    
if __name__ == "__main__":
    main()