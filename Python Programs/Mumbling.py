
# question link : https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(s):
    return '-'.join((char*index).capitalize() for index,char in enumerate(iterable=s,start=1))
    

print(accum("RqaEzty"))