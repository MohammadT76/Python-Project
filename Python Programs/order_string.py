
# question link : https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

import re

def order(sentence):
    if sentence == '':
        output = ''
    else:
        split_string = sentence.split(' ')
        find_num = re.findall(r'\d+', sentence)
        dictionary = {split_string[i]:find_num[i] for i in range(len(split_string))}
        sorting = sorted(dictionary.items(),key = lambda item:item[1])
        output = ' '.join(word[0] for word in sorting)
    return output
    
    
# solution 2
def order_v2 (words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
    
print(order_v2("is2 hello5 Thi1s T4est 3a"))
# print(order_v2(""))