
# question link : 
# https://www.codewars.com/kata/520446778469526ec0000001/train/python

'''
# some examples for this function :
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''

import numpy as np

def same_structure_as(original,other):
    if type(original) != type(other) or len(original) != len(other):
        return False
    for org_val, other_val in zip(original, other):
        # if type(org_val) != type(other_val):
        #     return False
        if isinstance(org_val,int) and isinstance(other_val,int):
            continue
        else:
            # if len(str(org_val)) != len(str(other_val)):
            #     return False
            if isinstance(org_val,list) and isinstance(other_val,int) or\
               isinstance(org_val,int) and isinstance(other_val,list) or\
               isinstance(org_val,tuple) and isinstance(other_val,int) or\
               isinstance(org_val,int) and isinstance(other_val,tuple):
                return False
            if type(org_val) is list and type(other_val) is list:
                if not same_structure_as(org_val, other_val):
                    return False
    return True


# print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
# print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

# original = [15, 14, 5, [20, [14, 14], -15, [1, [10, [18, 1, 2, -20]]]], -6, -2, [10, 5, -15, 11], 2, 8, -8, -17, [-2, -15, 4, 7], -3, -14, -18, 20, 3, 14, [14, -7, -1, -3], 8, -13, [[11, 2, 8, 14], 5, -13, [-1, [-13, 3]]], 7, -15, -8, -19, -10, -17] 
# other = [0, -17, 1, [-3, [0, -9], -6, [16, [-5, [-16, 11, -9, 20]]]], -14, 9, [19, 18, 15, 1], 0, -10, -20, -4, [20, -1, -8, 1], 3, -11, -20, 17, -2, 10, [-6, -3, 5, 16], 6, 19, [[1, 13, 15, 16], -15, -10, [-10, [20, 14]]], 15, 11, 20, -19, 11, -7] 

# print(same_structure_as(original, other))
# print(same_structure_as([1,[1,1]], [2,[2]]))
# print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
