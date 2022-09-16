
# question link : https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
# usefull link : 
# https://www.adamsmith.haus/python/answers/how-to-check-if-a-string-contains-a-number-in-python
# https://www.w3schools.com/python/ref_string_rstrip.asp
# https://www.geeksforgeeks.org/python-program-to-increment-suffix-number-in-string/

import re

def increment_string(string):
    if any(map(str.isdigit, string)):
        pass
    else:
        string += '0'
    # fstring used to form string
    # zfill fills values post increment
    result = re.sub(r'[0-9]+$',
                    lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}",
                    string)
    return str(result)

# solution 2
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

test = "foobar001"
# test = "foobar"
print(increment_string(test))
