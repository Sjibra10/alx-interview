#!/usr/bin/python3
"""interview question lockbozxes"""


def canUnlockAll(boxes):
    """unlock boxes"""
    if not boxes:
        return False

    opened_boxes = {0}

    keys = set(boxes[0])

    while keys:
        current_key = keys.pop()

        if current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys.update(boxes[current_key])

    return len(opened_boxes) == len(boxes)
