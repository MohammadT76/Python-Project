
# question link : https://www.codewars.com/kata/5816b76988ca9613cc00024f/train/python
# example) a = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
#          r = [1, 2, 3, 0, 1, 3, 5, 0, 2, 4, 8, 0, 4, 5, 6, 0]
#          test.assert_equals(sort_sequence(a), r)

def sort_sequence(sequence):
    a = ''.join(str(num) for num in sequence)
    b = a.split('0')
    c = [sorted(x) for x in b]
    print(b)

a = [3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]
sort_sequence(a)