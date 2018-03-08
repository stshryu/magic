import sys
from functools import reduce

def lonelyinteger(arr):
    return(reduce(lambda x, y: x ^ y, arr))
