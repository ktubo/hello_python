"""
From CodeWars:

The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Created by: Kira Tubo
Completed on: Apr 20, 2023
"""


def duplicate_encode(word):
    word = word.lower()  # stores word in all lower case
    temp_list = []  # to store each letter as a list item
    for letter in word:
        temp_list += letter

    new_string = ""
    for letter in word:
        count_letters = temp_list.count(letter)  # counts number of instances the letter shows up in list
        if count_letters <= 1:
            new_string += "("
        else:
            new_string += ")"
    return new_string


test_word = "Success"
print(duplicate_encode(test_word))


"""

#A more elegant solution: 

def duplicate_encode(word):
    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("
            
    return result
"""


"""
#Updated original code to use .count() for string instead of list
def duplicate_encode2(word):
    word = word.lower()  # stores word in all lower case
    new_string = ""

    for letter in word:
        count_letters = word.count(letter)  # counts number of instances the letter shows up in string
        if count_letters <= 1:
            new_string += "("
        else:
            new_string += ")"

    return new_string
"""