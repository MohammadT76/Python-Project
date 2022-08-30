
# question link : https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python 
# usefull link : https://stackoverflow.com/questions/42956690/python-periodically-remove-items-from-a-list


def remove_every_other(my_list):
    a, b = 1, 1
    r = [x for i, x in enumerate(my_list) if i%(a+b) < a]
    return r

# solution 2
def remove_every_other(my_list):
    return my_list[::2]

#%%
l = range(1, 30)
a, b = 5, 7
# r = [x for i, x in enumerate(l) if i%(a+b) < a]
for i,x in enumerate(l):
    if i%(a+b) < a:
        print(x)
print(r)
# [1, 2, 3, 4, 5, 13, 14, 15, 16, 17, 25, 26, 27, 28, 29]