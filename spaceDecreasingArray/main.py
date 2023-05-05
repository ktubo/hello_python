"""
From CodeWars: Running out of space

Kevin is noticing his space run out! Write a function that removes the spaces from the values
and returns an array showing the space decreasing.

For example, running this function on the array ['i', 'have','no','space']
would produce ['i','ihave','ihaveno','ihavenospace']

Created by Kira Tubo
Completed Apr 21, 2023
"""


def spacey(array):
    new_array = []
    concat_str = ""
    for i in array:
        new_array.append(concat_str + i)
        concat_str += i  # adds current list item to str, to be used in next list item
    return new_array


test_array = ['I', 'am', 'test']
print(spacey(test_array))

test_array2 = ['I']
print(spacey(test_array2))
