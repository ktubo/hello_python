"""
From CodeWars:
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each other and
preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

Created by Kira Tubo
Completed Apr 20, 2023
"""


def unique_in_order(sequence):
    new_list = []
    current_list = []

    # if list is empty
    if sequence == "" or sequence == [] or sequence == ():
        return new_list

    # convert data type of input to list
    if type(sequence) is str:
        current_list = sequence
    elif type(sequence) is list or type(sequence) is tuple:
        for i in range(len(sequence)):
            current_list.append(sequence[i])

    # if list contains only one value
    if len(current_list) == 1:
        new_list.append(current_list[0])
        return new_list

    # add value in index 0 by default before adding other values in list
    new_list.append(current_list[0])

    # adds other values in list
    for i in range(len(current_list)-1):  # stops loop before 2nd to last index
        if current_list[i] == current_list[i+1]:
            # if the values in current and next index match, continue to next iteration
            continue
        else:
            # if the values in current and next index do not match, add the value of next index to list
            new_list.append(current_list[i+1])
    return new_list


test_sequence = "Ab"
print(unique_in_order(test_sequence))

test_sequence2 = ['a', 'b', 'b', 'C']
print(unique_in_order(test_sequence2))

test_sequence3 = ('a', 'b', 'b', 'D')
print(unique_in_order(test_sequence3))

test_sequence4 = [1, 2, 2, 4, 99, -1, -1]
print(unique_in_order(test_sequence4))

test_sequence5 = [1]
print(unique_in_order(test_sequence5))

"""
#A better solution:

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
    """
