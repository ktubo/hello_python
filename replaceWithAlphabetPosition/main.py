"""
From CodeWars: Replace with Alphabet Position

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

Created by Kira Tubo
Completed on Apr 23, 2023
"""
def alphabet_position(text):
    # added placeholder for position 0 so that 'a' can start in position 1
    alphabet_lower = '0abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str = ''

    for i in text:
        # start looking at alphabet string at position 1
        if i in alphabet_lower[1:]:
            new_str += str(alphabet_lower.index(i)) + " "
        elif i in alphabet_upper[1:]:
            new_str += str(alphabet_upper.index(i)) + " "

    return new_str[0:-1]  # removes trailing space at the end of the sentence


"""
# Another solution:
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')

"""







str1 = "This is a test"
print(alphabet_position(str1))

