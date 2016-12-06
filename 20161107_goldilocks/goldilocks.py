"""
Solution for the goldilocks problem.
"""

import sys

def solve(weight, temperature, array):
    """
    Enumerate the array to find those entries that satisfy
    Goldilocks' weight/temperature requirements.
    """
    goodIdxs = []
    for idx, val in enumerate(array):
        if val[0] >= weight and val[1] <= temperature:
            goodIdxs.append("{}".format(idx + 1))
    return goodIdxs

_LINES = [[int(val) for val in line.strip().split(' ')] for line in sys.stdin.readlines()]

print("{}".format(' '.join(solve(_LINES[0][0], _LINES[0][1], _LINES[1:]))))
