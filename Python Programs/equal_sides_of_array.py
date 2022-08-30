
# question link : https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/python

from time_consuming_decorator import timer_func , timer_func_v2

@timer_func_v2
def find_even_index(arr):
    for x in range(len(arr)):
        if sum(i for i in arr[:x]) == sum(j for j in arr[x+1:]):
            return x
    return -1
    
arr = [10,-80,10,10,15,35,20]
print(find_even_index(arr))