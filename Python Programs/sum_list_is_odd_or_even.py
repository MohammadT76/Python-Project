
# this function getting a list of integers and if sum(list)%2 == 0 then return 'even'
# otherwise return 'odd'

test = [0, -1, -5]
test = []
test = [1,1,1,1,1]

def odd_or_even(arr):
    if arr is None:
        arr = [0]
    return 'even' if not sum(arr)%2 else 'odd'

print(odd_or_even(test))