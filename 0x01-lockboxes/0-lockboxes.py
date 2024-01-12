#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """method that determines if all the boxes can be opened"""
    if not boxes:
        return False
    n = len(boxes)
    unlocked = set()

    def search(box):
        """ add unlocked boxes"""
        unlocked.add(box)
        for i in boxes[box]:
            if 0 <= i < n and i not in unlocked:
                search(i)
    search(0)
    return len(unlocked) == n
