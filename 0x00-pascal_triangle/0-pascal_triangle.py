#!/usr/bin/env python3
"""
Contains a function pascal_triangle(n)
"""


def pascal_triangle(n):
    """creates a pascal triangle"""
    if n <= 0:
        return []
    
    p_triangle = []
    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
        else:
            previous_row = p_triangle[i - 1]
            row.append(1) #first element is always 1
            for j in range(1, i):
                element = previous_row[j - 1] + previous_row[j]
                row.append(element)
            row.append(1) #last element is always 1
        p_triangle.append(row)
    return p_triangle
