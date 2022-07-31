# question link in codewars:
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

# solution 1
def open_or_senior_v1 (data):
    li = []
    for member in data:
        if member[0] >= 55 and member[1] > 7:
            li.append('Senior')
        else:
            li.append('Open')
    return li

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior_v1(input))


# solution 2
def open_or_senior_v2 (data):
  return ['Senior' if age>=55 and handicap>7 else 'Open' for age,handicap in data]

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior_v2(input))