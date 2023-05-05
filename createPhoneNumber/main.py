"""
From Code Wars: Create Phone Number

Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!

Created by Kira Tubo
Completed Apr 21, 2023
"""


def create_phone_number(n):
    temp_list = n
    num_str = ""

    if len(n) != 10:
        return "Phone number must be 10 digits"

    # makes sure contents of list has integers
    for i in n:
        if type(i) is not int:
            return "Phone number needs to have digits"

    # inserts formatting into list
    temp_list.insert(0, '(')
    temp_list.insert(4, ')')
    temp_list.insert(5, ' ')
    temp_list.insert(9, '-')

    # stores list into a string
    for i in temp_list:
        num_str += str(i)

    return num_str


test_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(test_num))

test_num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(create_phone_number(test_num2))

test_num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a']
print(create_phone_number(test_num3))

"""
# A solution that uses slices:

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

# A solution that uses .format function

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
"""
