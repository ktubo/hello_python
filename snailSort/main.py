"""
NOTE:NOT COMPLETE
"""

def snail(snail_map):
    array = []

    if snail_map == [[]]:
        return array


    last_col = [row[len(snail_map[0])-1] for row in snail_map]
    return last_col
    """return row[snail_map]
    array = snail_map[0]
    array.append(snail_map[1][2])
    return array"""

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(snail(a))

a = [[]]
print(snail(a))

a = [[1]]
print(snail(a))
