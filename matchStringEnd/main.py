"""
From CodeWars: String ends with?

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

Created by Kira Tubo
Completed on Apr 23, 2023
"""


def solution(text, ending):
    #  start of slice is full length of text minus length of ending
    if ending == text[len(text)-len(ending):]:
        return True
    else:
        return False


string = "samurai"
end = "ai"
print(solution(string,end))

string = "sumo"
end = "omo"
print(solution(string,end))

"""
# Another solution

def solution(string, ending):
    return string.endswith(ending)
"""