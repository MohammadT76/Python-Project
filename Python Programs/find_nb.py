 
# question link : 
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# ex) find_nb (1071225) --> 45
# useful link : 
# https://math.stackexchange.com/questions/294213/prove-that-13-23-n3-1-2-n2

import math

def find_nb_v1 (m):
    threshold = math.sqrt(m)  
    if (threshold)%1 == 0:  
        result = 0
        n = 1
        while True:
            result = result + n
            if result == threshold:
                return n
            elif result != threshold:
                n += 1
            elif result > threshold:
                return -1
    else:
        return -1
   
# checking for running time
import time
start_time = time.time()
print(find_nb_v1 (135440716410000))   
print("--- %s seconds ---" % (time.time() - start_time))

#%%
# solution 2
# import math

# def find_nb_v2 (m):
#     result = 0
#     n = 1
#     # threshold = math.sqrt(m)
#     threshold = m**(1/2)   
#     if (threshold)%1 == 0:  
#         while True:
#             # result = pow(n,2) + n - 2*math.sqrt(m)
#             result = sum(x for x in range(1,n+1))
#             if result == threshold:
#                 return n
#             elif result != threshold:
#                 n += 1
#             elif result > threshold:
#                 n = -1
#                 break
#     else:
#         n = -1
#     return n

# print(find_nb_v2(91716553919377))  

#%%
# solution 3

def find_nb_v2 (m):
    n = 1
    volum = 0
    while volum < m:
        volum += n**3
        if volum == m:
            return n
        n += 1
    return -1

import time
start_time = time.time()
print(find_nb_v2 (135440716410000))   
print("--- %s seconds ---" % (time.time() - start_time))