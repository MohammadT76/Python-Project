
# question link : https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

def is_anagram(test, original):
    return True if sorted(list(test.lower())) == sorted(list(original.lower())) else False



# print(is_anagram('mohammad','hammadom'))
print(is_anagram('Buckethead', 'DeathCubeK'))