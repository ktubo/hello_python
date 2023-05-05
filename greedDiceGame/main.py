"""
From CodeWars: Greed is Good

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll.
For example, a given "5" can only count as part of a triplet (contributing to the 500 points)
or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
In some languages, it is possible to mutate the input to the function.
This is something that you should never do.
If you mutate the input, you will not be able to pass all the tests.

Created by Kira Tubo
Completed Apr 22, 2023
"""


def score(dice):
    count1 = dice.count(1)
    count2 = dice.count(2)
    count3 = dice.count(3)
    count4 = dice.count(4)
    count5 = dice.count(5)
    count6 = dice.count(6)
    total = 0

    if count1 >= 3:
        total += 1000
        if count1 == 4:
            total += 100
        if count1 == 5:
            total += 100*2

    if count5 >= 3:
        total += 500
        if count5 == 4:
            total += 50
        if count5 == 5:
            total += 50*2

    if count6 >= 3:
        total += 600
    if count4 >= 3:
        total += 400
    if count3 >= 3:
        total += 300
    if count2 >= 3:
        total += 200

    for i in dice:
        if count1 < 3 and i == 1:
            total += 100
        if count5 < 3 and i == 5:
            total += 50

    return total


d = [1, 1, 1, 1, 1]
print(score(d))

d = [5, 5, 1, 1, 1]
print(score(d))

d = [5, 5, 2, 1, 2]
print(score(d))

d = [5, 6, 6, 6, 2]
print(score(d))

d = [2, 2, 2, 2, 2]
print(score(d))

"""
#Another solution:
def score(dice):
    total = 0
    for d in range(1, 7):
        count = dice.count(d)
        if count >= 3:
            total += 1000 if d == 1 else d * 100
            count -= 3
        total += 100 * count if d == 1 else 50 * count if d == 5 else 0
    return total
"""