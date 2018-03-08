import sys

def maximizingXor(l, r):
    k = 0
    for i in range(l, r + 1):
        for y in range(l, r + 1):
            x = i ^ y
            if k < x:
                k = x
    return k
