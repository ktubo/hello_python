"""
From CodeWars: Take a Ten Minute Walk
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment,
so you decided to take the opportunity to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones --
everytime you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block for each letter (direction)
and you know it takes you one minute to traverse one city block,
so create a function that will return true if the walk the app gives you
will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing
a random assortment of direction letters ('n', 's', 'e', or 'w' only).
It will never give you an empty array (that's not a walk, that's standing still!).

Created by Kira Tubo
Completed Apr 21, 2023
"""


def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        count_n = walk.count('n')
        count_s = walk.count('s')
        count_e = walk.count('e')
        count_w = walk.count('w')

    if (count_n == 4 and count_s == 4 and count_e == 1 and count_w == 1) or \
            (count_n == 1 and count_s == 1 and count_e == 4 and count_w == 4) or \
            (count_n == 3 and count_s == 3 and count_e == 2 and count_w == 2) or \
            (count_n == 2 and count_s == 2 and count_e == 3 and count_w == 3) or \
            (count_n == 5 and count_s == 5) or (count_e == 5 and count_w == 5):
        return True
    else:
        return False


test_walk1 = ['w','e','w','e','w','e','w','e','w','e','w','e'] # returns false because too long
print(is_valid_walk(test_walk1))

test_walk2 = ['w']  # returns false because too short
print(is_valid_walk(test_walk2))

test_walk3 = ['n','n','n','s','n','s','n','s','n','s']  # returns false because doesn't match count
print(is_valid_walk(test_walk3))

test_walk4 = ['n','s','n','s','n','s','n','s','n','s']  # returns true
print(is_valid_walk(test_walk4))


"""
# Another solution:
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False
"""

