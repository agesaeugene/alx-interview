#!/usr/bin/python3
"""
 Each box is sequentially numbered from 0 to n-1,
 and each box may hold keys to the other boxes.
"""
def canUnlockAll(boxes):
    """
    Descriiption:
    Method to determine if all boxes can be opened
    Arguments: boxes --> List of Lists, which
    includes boxes with keys.
    Return a boolean. Variables:
    MyKeys -> List, Store the number keys for opening
    boxes.
    key --> integer, key from myKeys box.Key -> integer,
    key inside a certain box.

    """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes [key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False
