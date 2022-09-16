
# question link : https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    vowels_char = ['a','e','i','o','u']
    return sum(sentence.lower().count(i) for i in set(sentence) if i in vowels_char)


test = 'aeifdsafasf32432 3f fdsfds ou'
print(get_count(test))


