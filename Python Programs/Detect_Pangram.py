
# question link : https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# for generating all english's alphabet
# usefull link : https://stackoverflow.com/questions/16060899/alphabet-range-in-python
import string

def is_pangram(s):
    all_alph = string.ascii_lowercase
    # putting all char in s that is alphabet and remove other char from s
    all_alph_in_s = [char for char in set(s.lower()) if char.isalpha()]
    return True if len(all_alph) == len(all_alph_in_s) else False

# solution 2
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())

s = "The quick brown fox jumps over the lazy dog"
s = "1bcdefghijklmnopqrstuvwxyz"

print(is_pangram(s))

