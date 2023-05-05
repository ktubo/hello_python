"""
From CodeWars:
Please write a function that sums a list, but ignores any duplicate items in the list.
For instance, for the list [3, 4, 3, 6] , the function should return 10.

Created by Kira Tubo
Completed Apr 21, 2023
"""

def sum_no_duplicates(l):
    total = 0
    for num in l:
        # counts the number of instances the number appears in the list
        count_num = l.count(num)
        # only adds the number if it appears once in the list
        if count_num == 1:
            total += num
    return total


test_list = [5, 3, 1, 5, 6, 7, 2, 4, 3, 2]
print(sum_no_duplicates(test_list))


"""
Another solution: 
def sum_no_duplicates(l):
    new = []
    for x in l:
        if l.count(x) == 1:
            new.append(x)
    return sum(new)
"""