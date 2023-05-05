"""
From CodeWars:
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

Created by Kira Tubo
Completed on Apr 21, 2023
"""


def find_short(s):
    temp_list = s.split()
    l = len(temp_list[0])  # initially store the length of the first word in the list

    for word in temp_list:
        if l > len(word):
            l = len(word)

    return l # l: shortest word length


test_string = "hello how are you today in here"
print(find_short(test_string))

"""
Alternative solution with min():

def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length
"""