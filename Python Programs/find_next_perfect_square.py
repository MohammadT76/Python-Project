# question link : 
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math

# solution 1
def find_next_square_v1 (sq):
    return pow(int(math.sqrt(sq))+1,2) if pow(int(math.sqrt(sq)),2) == sq else -1


print(find_next_square_v1(122))
print(find_next_square_v1(625))


# solution 2
def find_next_square_v2 (sq):
    return pow(int(math.sqrt(sq))+1,2) if pow(int(sq**(1/2)),2) == sq else -1


print(find_next_square_v1(122))
print(find_next_square_v1(625))


# solution 3
def find_next_square_v3 (sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2

print(find_next_square_v1(122))
print(find_next_square_v1(625))