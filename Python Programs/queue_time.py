
# question link : 
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
#
# ex) queue_time([10,2,3,3], 2)
#     should return 10
#     because here n=2 and the 2nd, 3rd, and 4th people in the 
#     queue finish before the 1st person has finished.


def queue_time (customers, n):
    len_queue = len(customers)
    if n >= len_queue:
        return max(customers)
    else:
        while True:
            max_time = max(customers[0:n])
            customer_1 = customers[0]
            

print(queue_time([10,2,3,3], 5))