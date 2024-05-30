# Write your solution here
def find_words(search_term: str) -> list:
    """Returns every word that matches the search"""
    matched_words = []
    with open("words.txt") as file:
        if search_term[0] == "*":
            for word in file:
                word = word.strip()
                if word.endswith(search_term[1:]):
                    matched_words.append(word)
        elif search_term[-1] == "*":
            for word in file:
                word = word.strip()
                if word.startswith(search_term[:-1]):
                    matched_words.append(word)
        elif "." in search_term:
            length = len(search_term)
            for word in file:
                word = word.strip()
                if len(word) == length:
                    for i in range(length):
                        if search_term[i] == ".":
                            continue
                        else:
                            if word[i] != search_term[i]:
                                break
                    else:
                        matched_words.append(word)
        else:
            for word in file:
                word = word.strip()
                if word == search_term:
                    matched_words.append(word)
    
    return matched_words


if __name__ == "__main__":
    print(find_words("p.ng"))