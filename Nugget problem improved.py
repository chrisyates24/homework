# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:26:53 2016

@author: chris
"""

a=input("Input value for 'a' as the smallest single order of nuggets. a=")
b=input("Input value for 'b' as the medium sinigle order of nuggets. b=")
c=input("Input value for 'c' as the largest single order of nuggets. c=")

a=int(a)
b=int(b)
c=int(c)

def solution_nuggets(amt, nuggets, i=None):
    """
    Return True if any whole multiples of pieces[:i+1] sum to amt, else False
    """
    if i is None:
        i = len(nuggets) - 1   # start with last item
    n = nuggets[i]
    if i:
        return any(solution_nuggets(amt - n*k,nuggets, i-1) for k in range(amt // n + 1))
    else:
        return amt % n == 0

def find_max_unbuyable(nuggets):
    least = min(nuggets)
    p = 0
    last_unsolved = None
    consecutive = 0
    while consecutive < least:
        p += 1
        if solution_nuggets(p, nuggets):
            consecutive += 1
        else:
            last_unsolved = p
            consecutive = 0
    return last_unsolved

def main():
    nuggets = [a, b, c]
    max_unbuyable = find_max_unbuyable(nuggets)
    p=max_unbuyable
    print("Largest number of McNuggets that cannot be bought in exact quantity:",p)

if __name__=="__main__":
    main()
