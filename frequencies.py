"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter
def frequencies(items):
    frequencies = {}
    newlist = []
    for i in items:
        newlist.append(str(i))

    # Your code goes here
    return Counter(newlist)
