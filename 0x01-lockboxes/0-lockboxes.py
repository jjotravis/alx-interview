#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially
from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened
    """
    n = len(boxes)
    opened = set()
    keys = [0]

    while keys:
        current = keys.pop()

        if current not in opened:
            opened.add(current)
            keys.extend(k for k in boxes[current] if k not in opened)
    return len(opened) == n
