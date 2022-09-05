
# a = [1,2,3,2,1,5,6,5,5,5]

# import collections
# print([item for item, count in collections.Counter(a).items() if count > 1])

# test = [1, 2, 4, 5, 5]
# test = [3, 2, 5, 1, 3, 4]

# if len(set(test)) == max(test):
#     print('yes')
# else:
#     print('no')

#%%

from generate_random_number import gen_randint
start = 10
stop = 100000
num = 1000

# generating a list of random number for testing runing time for these functions
test = gen_randint(start,stop,num)
# test = [1,2,3,4,5,6,3,6,3]

# question link : https://www.codewars.com/kata/558dd9a1b3f79dc88e000001/train/python
from time_consuming_decorator import timer_func_v2
import collections

@ timer_func_v2
def find_dup(arr):
    return [item for item, count in collections.Counter(arr).items() if count > 1]

# solution 2
@ timer_func_v2
def find_dup_v2 (arr):
    return max([i for i in arr if arr.count(i) > 1])

print(find_dup(test))
print(find_dup_v2(test))