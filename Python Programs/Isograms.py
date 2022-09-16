
# question link : https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    for char in set(string.lower()):
        if (string.lower()).count(char) > 1 and char.isalpha():
            return False
    return True

# solution 2
def is_isogram_v2 (string):
    return len(string) == len(set(string.lower()))

string = 'abc  d '
print(is_isogram(string))

