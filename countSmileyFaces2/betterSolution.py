"""
One solution found in CodeWars by FabioRosado
"""

def count_smileys_better(arr):
    total = 0
    eyes = ':;'
    nose = '-~'
    mouth = ')D'
    new_str = ""
    for char in arr:
        if len(char) == 3:
            if char[0] in eyes and char[1] in nose and char[2] in mouth:
                total += 1

        elif len(char) == 2:
            if char[0] in eyes and char[1] in mouth:
                total += 1
    return total

test_better = [":)", ";D"]
#print(count_smileys_better(test_better))
