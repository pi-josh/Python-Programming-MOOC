# Write your solution here
def same_chars(string, index1, index2):
    if not index1 < len(string) or not index2 < len(string):
        return False
    elif string[index1] == string[index2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))