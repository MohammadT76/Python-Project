
# some other useful links : 
# https://stackoverflow.com/questions/49182242/python-remove-one-of-two-duplicates-next-to-each-other-in-a-list

test = 'AAAABBBCCDAABBB'
test = [1,2,2,3,3]
test = 'ABBCcAD'

def unique_in_order_v1 (iterable):
    li = list(iterable)
    return [li[i] for i in range(0,len(li)) if i == 0 or li[i] != li[i-1]]

print(unique_in_order_v1(test))


# solution 2
from itertools import groupby

def unique_in_order_v2 (iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order_v2(test))