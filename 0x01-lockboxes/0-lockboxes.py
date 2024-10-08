#!/usr/bin/python3
"""Unlocks List of lists"""


def canUnlockAll(boxes):
    """
    Input: List of Lists

    Output: Unlocks other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
