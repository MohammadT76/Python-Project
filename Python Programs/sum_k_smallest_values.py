# this function getting a list of numbers (all values are positive or 0) ,
# then find k smallest values in this list and return sum of thes values

# solution 1
import heapq

def sum_k_smallest (input_list , k):
    # this line return a list that contains of k smallest values in the original list
    k_smallest = heapq.nsmallest(k, input_list)
    return sum(k_smallest)

input_list = [10, 343445353, 3453445, 3453545353453]
k = 2

print(sum_k_smallest(input_list , k))


# solution 2
def sum_k_smallest_v2 (input_list , k):
    return sum(sorted(input_list)[:k])

print(sum_k_smallest_v2(input_list , k))
