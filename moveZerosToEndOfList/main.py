"""
From CodeWars:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

Created by Kira Tubo
Completed on Apr 21, 2023
"""

def move_zeros(lst):
    count_zeros = lst.count(0)
    new_list = []
    for num in lst:
        if num != 0:
            new_list.append(num)
    for i in range(count_zeros):
        new_list.append(0)
    return new_list


test_list = [0, 1, 4, 2, 0, 1, 0]
print(move_zeros(test_list))

"""
# Another solution for removing and adding 0 to same list:

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array
"""