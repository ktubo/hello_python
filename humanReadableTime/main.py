"""
From CodeWars: Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Created by: Kira Tubo
Completed on: Apr 22, 2023

"""


def make_readable(s):
    # converts seconds to minutes
    m = s // 60
    h = 0
    s = s - (60 * m)  # deducts amount converted to minutes

    # converts minutes to hours
    if m >= 60:
        h = m // 60
        m = m - (60 * h)  # deducts amount converted to hours

    return "%02d:%02d:%02d" % (h, m, s)


sec = 60
print(make_readable(sec))

"""
# Another solution:
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""