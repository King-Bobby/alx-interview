#!/usr/bin/python3
"""
Contains the function canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is open by default

    keys = [0]  # Start with the keys in the first box

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key >= 0 and key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
