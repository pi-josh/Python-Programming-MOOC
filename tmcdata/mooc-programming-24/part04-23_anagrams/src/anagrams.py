# Write your solution here
def anagrams(string1: str, string2: str):
    return True if sorted(string1) == sorted(string2) else False