
# question link : https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

from time_consuming_decorator import timer_func

@timer_func
def row_sum_odd_numbers(n):
    starting_odd_number = sum(range(1,n))
    specific_odd_numbers = [2*x-1 for x in range(starting_odd_number+1,starting_odd_number+n+1)]
    return sum(specific_odd_numbers)    
      
      
# solution 2   
@timer_func
def row_sum_odd_numbers_v2 (n):
    print(n ** 3)
    return n ** 3

      
row_sum_odd_numbers_v2(2)