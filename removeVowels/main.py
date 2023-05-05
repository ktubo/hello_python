"""
From CodeWars: Disemvowel Trolls

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

Created by Kira Tubo
Completed on Apr 21, 2023
"""


def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_str = ""
    for i in string_:
        if i not in vowels:  # compare each letter in original to each letter in string of vowels
            new_str += i
    return new_str


test_str = "This website is for losers LOL"
print(disemvowel(test_str))


"""
Other solutions:
def disemvowel(string):
        
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
"""