"""
From CodeWars: ROT13

How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

Created by Kira Tubo
Completed on Apr 24, 2023
"""


def rot13(message):
    decoded = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    encoded = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    new_str = ''

    # My new solution using only one for loop
    for char in message:
        if char.isalpha() is False:
            new_str += char
        elif char in decoded:
            # uses the index of the char in decoded string
            new_str += encoded[decoded.index(char)]
    return new_str

    # My original Solution: I wasn't too happy with this one because it used additional for loops
    """for item in message:
        # handles non-alphabetic characters
        if item.isalpha() is False:
            new_str += item
        else:
            # uses index of decoded string for encoded string
            for i, char in enumerate(decoded):
                if item == char:
                    new_str += encoded[i]
    return new_str"""

m = 'hello 123 @#$jfiwe.'
print(rot13(m))

"""
# Another solution:
import string

def rot13(message):
	first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
   	trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
	return message.translate(string.maketrans(first, trance))  

"""