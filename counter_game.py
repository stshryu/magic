import sys

def power2(n):
    while(n != 0):
        p = n
        n = int(n) & int(n-1) # cast to int because of issues with Hackerrank
        # n = n & (n-1)
    return p

def win(n):
    richard = True
    while(n > 1):
        p = power2(n)
        if n == p:
            n /= 2
        else:
            n -= p
        richard = not richard
    return 'Richard' if richard else 'Louise'
