
# for more information see this link : https://www.tutorialspoint.com/generating-random-number-list-in-python

import random

def gen_randint(start,stop,num):
    #Generate 5 random numbers between 10 and 30
    randomlist = random.sample(range(start,stop), num)
    return randomlist