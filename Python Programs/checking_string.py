
#%%
# how can i generate english alphabet in specific range ? range(a:m)
list(map(chr, range(ord('a'), ord('m')+1)))

#%%
import string
string.ascii_lowercase
list(string.ascii_lowercase)
# %%


# question link : 
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

test = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

def printer_error_v1(s):
    # generate char range
    li_char = list(map(chr, range(ord('a'), ord('m')+1)))
    # counting number of errors
    err_count = sum(1 for char in list(s) if char not in li_char)
    return f"{err_count}/{len(list(s))}"


print(printer_error_v1(test))
    

#%%
# solution 2
from re import sub

test = "aaaaaayyaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"

def printer_error_v2 (s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

print(printer_error_v2(test))

# %%
