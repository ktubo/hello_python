"""
From CodeWars: Range Extraction

A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org

Created by Kira Tubo
Completed Apr 23, 2023
"""


def solution(args):
    index = 0
    is_range_start = True  # determines start of range
    new_list = []
    counter = 0

    for i in args[:-1]:
        # only prints start of range
        if args[index+1] - args[index] == 1 and is_range_start is True:
            new_list.append(i)
            new_list.append('-')  # marks as a range
            is_range_start = False  # skips rest of numbers within the range
            counter += 1

        # add number if it is either last number in range, or not part of range
        if args[index+1] - args[index] != 1:
            new_list.append(i)
            is_range_start = True  # resets endpoint for when another range occurs in list

        index += 1

    new_list.append(args[len(args)-1])  # adds last item to the list

    """There is an issue with the above code, in that numbers that are next to each other (e.g. (4,5))
    are being printed as a range e.g. (4-5), when the requirement is to not print them as a range, as 
    opposed to separating them with commas. The code below fixes this issue. 
    Admittedly, there is probably a better way to do this without resorting to another loop."""

    """The reason why I created a new list, as opposed to a string, was so that I could compare 
    integers that were being separated by a dash (-). If the above code met the requirements as is, 
    I would have added to a string instead"""

    index2 = 0
    new_string = ''

    for i in new_list[:-1]:
        if type(i) is int and type(new_list[index2+1]) is int:
            new_string += str(i) + ','
        elif type(i) is int:
            new_string += str(i)
        elif type(i) is not int:
            # this is to compare the numbers marked as a range with the dash (-) symbol
            temp_num1 = new_list[index2-1]
            temp_num2 = new_list[index2+1]
            if temp_num2 - temp_num1 != 1:  # if the range between numbers is more than 1, keep string as range
                new_string += '-'
            else:
                new_string += ','
        index2 += 1

    new_string += str(new_list[len(new_list)-1])  # adds last item in list to string

    return new_string


pos_num = [0, 1, 2, 4, 5, 9, 11, 13, 14, 15]
print(solution(pos_num))

neg_num = [-10,-9,-7,-6,-4,-3,-2,0,1]
print(solution(neg_num))

all_num = [-9,-6,-5,-1,0,1,3,5]
print(solution(all_num))


"""
Another solution:
def solution(args):
    result = ""
    i = 0
    while i<len(args):
        val = args[i]
        while i+1<len(args) and args[i]+1==args[i+1]:
            i+=1
        if val == args[i]:
            result += ",%s"%val
        elif val+1 == args[i]:
            result += ",%s,%s"%(val, args[i])
        else:
            result += ",%s-%s"%(val, args[i])
        i+=1
    return result.lstrip(",")
"""