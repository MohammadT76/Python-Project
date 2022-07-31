# question link:
# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python


# solution 1
def get_sum_v1 (a,b):
    return sum(x for x in range(min(a,b),max(a,b)+1)) if a != b else a

print(get_sum_v1(1, 1))


# solution 2
def get_sum_v2 (a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum_v2(1, 1))