"""
From CodeWars: Who likes it?

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.

Created by: Kira Tubo
Completed on: Apr 21, 2023
"""


def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return "%s likes this" % str(names[0])
    if len(names) == 2:
        return "%s and %s like this" % (str(names[0]), str(names[1]))
    if len(names) == 3:
        return "%s, %s and %s like this" % (str(names[0]), str(names[1]), str(names[2]))
    else:
        count_extra_names = len(names)-2
        return "%s, %s and %s others like this" % (str(names[0]), str(names[1]), str(count_extra_names))


empty_list = []
print(likes(empty_list))

one_name = ["Vivian"]
print(likes(one_name))

two_names = ["Vivian", "John"]
print(likes(two_names))

three_names = ["Vivian", "John", "Mark"]
print(likes(three_names))

four_names = ["Vivian", "John", "Mark", "Stephen"]
print(likes(four_names))

five_names = ["Vivian", "John", "Mark", "Stephen", "David"]
print(likes(five_names))


"""
Another solution using dictionaries:
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)
"""