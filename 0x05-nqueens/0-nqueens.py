#!/usr/bin/python3
"""
N queens solution finder
"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)


def solve_nqueens(x):
    '''self descriptive'''
    if x == 0:
        return [[]]
    inner_solution = solve_nqueens(x - 1)
    return [solution + [(x, i + 1)]
            for i in range(n)
            for solution in inner_solution
            if safe_queen((x, i + 1), solution)]


def attack_queen(square, queen):
    '''Checks if the positions of two queens are in an attacking mode.'''
    (row, col) = square
    (row, col) = queen
    return (row == row) or (col == col) or\
        abs(row - row) == abs(col - col)


def safe_queen(sqr, queens):
    '''self descriptive'''
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True


for answer in reversed(solve_nqueens(n_q)):
    result = []
    for p in [list(p) for p in answer]:
        result.append([i - 1 for i in p])
    print(result)
