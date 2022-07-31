# this function getting a list of numbers then 
# count positive number and calculate sum of the negetive number
# Note : 0 is neither positive nor negative

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
test = [0]

# solution 1
def count_positives_sum_negatives_v1 (arr):
    count_pos = 0
    sum_neg = 0
    if arr == []:
        return []
    else:
        for num in arr:
            if num > 0:
                count_pos += 1
            elif num < 0:
                sum_neg = sum_neg + num
        return [count_pos,sum_neg]

print(count_positives_sum_negatives_v1(test))


# solution 2
def count_positives_sum_negatives_v2 (arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

print(count_positives_sum_negatives_v2(test))