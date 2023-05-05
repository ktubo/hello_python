"""
From CodeWars: Mexican Wave
The wave (known as the Mexican wave in the English-speaking world outside North America)
is an example of metachronal rhythm achieved in a packed stadium
when successive groups of spectators briefly stand, yell, and raise their arms.
Immediately upon stretching to full height, the spectator returns to the usual seated position.

The result is a wave of standing spectators that travels through the crowd,
even though individual spectators never move away from their seats.
In many large arenas the crowd is seated in a contiguous circuit
all the way around the sport field, and so the wave is able
to travel continuously around the arena; in discontiguous seating arrangements,
the wave can instead reflect back and forth through the crowd.
When the gap in seating is narrow, the wave can sometimes pass through it.
Usually only one wave crest will be present at any given time in an arena,
although simultaneous, counter-rotating waves have been produced. (Source Wikipedia)

Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
You will be passed a string and you must return that string in an array
where an uppercase letter is a person standing up.

Rules
 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

Created by Kira Tubo
Completed on Apr 22, 2023

"""


def wave(people):
    new_list = []
    index = 0

    for seat in people:
        if seat == ' ':
            index += 1  # moves to next iteration
        else:
            # capitalizes letter at current iteration only
            new_str = people[:index] + people[index].upper() + people[index+1:]
            new_list.append(new_str)
            index += 1

    return new_list


one_word = "hello"
print(wave(one_word))

two_words = "hi there"
print(wave(two_words))

empty_str = ""
print(wave(empty_str))

extra_spaces = "  spaces  "
print(wave(extra_spaces))

sentence = "my dog is fat"
print(wave(sentence))


"""
#Another solution using enumerate:
def wave(st):
    ls = []
    for i,l in enumerate(st):
        if l != ' ':
            ls.append(st[:i]+st[i].upper()+st[i+1:])
    return ls
"""