#!/usr/bin/python3
"""
In a text file, there is only one character H. Your text editor
can only do two operations in this file: Copy All and Paste.
Creating a method that minimizes the amount of operations 
required to get exactly n H characters in a given number, n.
"""


def countProcess(num):
    """ Return list of process until n H number of times """
    count = 1
    p_list = []
    val = num
    while val != 1:
        count += 1
        if val % count == 0:
            while (val % count == 0 and val != 1):
                val /= count
                p_list.append(count)

    return p_list


def minOperations(n):
    """ Return sum of process until n H number of times """
    if n < 2 or type(n) is not int:
        return 0
    values = countProcess(n)
    return sum(values)
