
# question link : https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
# usefull link : https://www.pythonforbeginners.com/basics/count-occurrences-of-each-character-in-string-python

def count(string):
    all_char_in_str = list(set(string))
    num_all_char_in_str = [string.count(i) for i in all_char_in_str]
    return {all_char_in_str[i]:num_all_char_in_str[i] for i in range(len(all_char_in_str))}

# solution 2
from collections import Counter
def count(string):
    return Counter(string)

# solution 3
def count(string):
    return {i: string.count(i) for i in set(string)}

print(count('aba'))