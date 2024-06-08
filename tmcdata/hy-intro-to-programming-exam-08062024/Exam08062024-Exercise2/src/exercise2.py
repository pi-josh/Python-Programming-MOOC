# Write your solution to exercise 2 here
def conditional_convert(my_list, my_function, condition_function=None):
    new_list = []
    if condition_function:
        for item in my_list:
            if condition_function(item):
                item = my_function(item)
            new_list.append(item)
        return new_list
    else:
        for item in my_list:
            item = my_function(item)
            new_list.append(item)
        return new_list


def contains_letter_a(word):
    return 'a' in word


def convert_to_uppercase(word):
    return word.upper()


word_list = ['apple', 'banana', 'kiwi']
transformed_words = conditional_convert(word_list, convert_to_uppercase, contains_letter_a)
print(transformed_words)

word_list = ['apple', 'banana', 'kiwi']
transformed_words = conditional_convert(word_list, convert_to_uppercase)
print(transformed_words)