YES = 1
NO = 2
OK = 4
CANCEL = 8

def add_buttons(n):
    if(n & YES):
        print("Adding YES")
    if(n & NO):
        print("Adding NO")
    if(n & OK):
        print("Adding OK")
    if(n & CANCEL):
        print("Adding CANCEL")

# Example usage

add_buttons(YES | NO | CANCEL)

#> OUTPUT:
#> Adding YES
#> Adding NO
#> Adding CANCEL

# This works because each CONST defined has a unique 1 in each place of power of 2 in binary
# E.G. 1 = 0001, 2 = 0010, 4 = 0100, 8 = 1000. As a result passing an OR operator into our function returns this:
# add_buttons(1 | 2 | 8) => add_buttons(1011) which when evaulated by AND will perform 4 operations.
# 1. if(1011 & 0001)
# 2. if(1011 & 0010)
# 3. if(1011, 0100)
# 4. if(1011, 1000)
# You can see that only 1, 2, and 4 are true which is why only YES, NO and CANCEL are added.
# Using bitwise operators & and | is pretty neat.
