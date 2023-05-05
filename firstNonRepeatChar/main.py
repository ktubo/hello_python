"""
From CodeWars: First Non-repeating character

Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter.
For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters,
it should return an empty string ("") or None -- see sample tests.

Created by Kira Tubo
Completed on Apr 23, 2023
"""


def first_non_repeating_letter(string):
    # for empty strings
    if string == '':
        return ''

    # evaluates lower case so characters such as 't' and 'T' are counted as one letter
    lower_case = string.lower()
    index = 0
    for i in lower_case:
        if lower_case.count(i) == 1:
            return string[index]  # returns char of original string
        index += 1

    return ''  # catch-all for other cases e.g. string with repeating characters


test = 'sTresstRie'
print(first_non_repeating_letter(test))

"""
# Another solution:
def first_non_repeating_letter(string):
    
    s = string.lower()
    
    for i in string:
        if s.count(i.lower()) == 1:
            return i
    return ''
"""