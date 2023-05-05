"""
From CodeWars: WeIrD StRiNg CaSe

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

Created by Kira Tubo
Completed on Apr 21, 2023

"""

def to_weird_case(words):
    index = 0  # tracks index of character in each word
    new_string = ""

    for char in words:
        remainder = index % 2  # checks to see if character index position is even or odd number

        if char == " ":
            new_string += " "
            index = -1  # resets index back to 0 at start of new word
        elif remainder == 0:
            new_string += char.upper()
        else:
            new_string += char.lower()

        index += 1  # moves on to next character in word

    return new_string


test_str = "Weird string case"
print(to_weird_case(test_str))

empty_str = ""
print(to_weird_case(empty_str))

test_str2 = "THIs iS a TEST"
print(to_weird_case(test_str2))


"""
# Solution using booleans 

def to_weird_case(string):
    newstring = ''
    i = True
    for char in string:
        if i == True:
            newstring += char.upper()
            i = False
        elif i == False:
            newstring += char.lower()
            i = True
        if char == " ":
            newstring += ""
            i = True
    return newstring
        
# Solution using enumerate

def to_weird_case(string):
    answers = ''
    for word in string.split():
        for idx,char in enumerate(word):
            if idx % 2 == 0:
                answers += char.upper() 
            else:
                answers += char.lower() 
        answers += ' '
    return answers[:-1]
    
"""