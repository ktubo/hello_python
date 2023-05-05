"""
NOT COMPLETE: NEEDS REDO
"""

def next_bigger(n):
    num_str = str(n)
    new_num_str = ''
    index = 0
    for i, item in enumerate(num_str[:-1]):
        if i == 0:
            if item > num_str[i+1]:
                new_num_str += item + num_str[i+1]
                #num_str = new_num_str + num_str[i + 2:]
            else:
                new_num_str += num_str[i+1] + item
                #num_str = new_num_str + num_str[i + 2:]
        elif new_num_str[index] < num_str[i+1]:
            new_num_str += num_str[i+1]
            #num_str = num_str[:i-1] + num_str[i+1] + item + num_str[i + 1:]
        elif new_num_str[index] > num_str[i+1]:
            new_num_str += str(item)
            #num_str = num_str[:i-1] + item + num_str[i+1] #+ num_str[i + 1:]
        """if item < num_str[i+1]:
            continue"""
        index += 1
    return new_num_str

num = 1245
print(next_bigger(num))