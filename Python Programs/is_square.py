
# question link : https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

def is_square (n):    
    return False if ((abs(n)**(1/2)%1) or n < 0) else True

print(is_square(-1))


# solution 2
import math
def is_square_v2 (n):
    return n > -1 and math.sqrt(n) % 1 == 0