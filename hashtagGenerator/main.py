"""
From CodeWars: The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

Created by Kira Tubo
Created on Apr 22, 2023
"""


def generate_hashtag(s):
    if s == '':  # Handles empty string first
        return False

    new_list = s.split()  # Removes all leading and trailing spaces
    new_sentence = '#'  # Adds hashtag to start of string

    for i in new_list:
        # Capitalizes first letter in each list item, lower case for rest of word
        new_sentence += i[0].upper() + i[1:].lower()

    if len(new_sentence) > 140:  # Result cannot be more than 140 characters
        return False

    return new_sentence


string1 = "  hi  Hello  this    is tEST     "
print(generate_hashtag(string1))

string2 = ""
print(generate_hashtag(string2))

string3 = "This is a long sentence that is going to be more than 140 characters if I keep typing on my keyboard How many characters do I have now Know one knows I just have to keep typing to find out"
print(generate_hashtag(string3))

"""
# Another solution

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
    
"""
