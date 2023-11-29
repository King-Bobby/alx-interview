#!/usr/bin/python3
"""
Module to calculate the perimeter of the island
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island
    Args:
        grid (list): list of list of integers representing the island

    Returns:
        int: perimeter of the island
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
