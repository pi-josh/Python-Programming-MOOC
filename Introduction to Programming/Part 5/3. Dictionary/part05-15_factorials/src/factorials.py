# Write your solution here
def factorials(n: int) -> dict:
    new_dict = {}
    new_dict[1] = 1
    for i in range(2, n+1):
        new_dict[i] = new_dict[i - 1] * i
    return new_dict


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])