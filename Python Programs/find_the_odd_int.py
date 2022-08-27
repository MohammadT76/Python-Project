
# question link : https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    return [x for x in set(seq) if seq.count(x)%2][0]


# solution 2
from functools import reduce
import operator

def find_it_v2 (xs):
    return reduce(operator.xor, xs)

test = [1,2,2,3,3,3,4,3,3,3,2,2,1]
print(find_it(test))