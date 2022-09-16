
# question link : https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

import collections

def duplicate_count(text):
    # this line return a dictionary of all word that exist in text and number of occurance (case-insensitive)
    all_char_and_numchar = collections.Counter(text.lower())
    return sum(1 for k,v in (collections.Counter(text.lower())).items() if v>=2)

# solution 2
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

print(duplicate_count('dfasfsdaLKJLJLLJLJLJD45353453'))