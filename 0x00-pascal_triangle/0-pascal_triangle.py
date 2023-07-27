#!/usr/bin/python3
"""Defines a function that prints a pascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integer indicating a pascal triangle"""
    if n <= 0:
        return []
    triangle = []
    for index in range(n):
        outer_row = [1]

        if index > 0:
            prev_row = triangle[index - 1]
            for inner_index in range(1, index):
                outer_row.append(prev_row[inner_index - 1] +
                                 prev_row[inner_index])
            outer_row.append(1)
        triangle.append(outer_row)
    return triangle
