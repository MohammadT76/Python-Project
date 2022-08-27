
# question link : https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    return int(''.join(sorted(str(num),reverse=True)))


# solution 2
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')

print(descending_order(56464))