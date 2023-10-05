#!/usr/bin/python3
"""
Contains the function canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                stack.append(key)

    return all(visited)
