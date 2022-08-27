
# usefull link : https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

import math

def grow(arr):
    return math.prod(arr)


# solution 2
from functools import reduce

def grow_v2(arr):
    return reduce(lambda a,b:a*b , arr)    

test = [3, 2, 4]
print(grow_v2(test))