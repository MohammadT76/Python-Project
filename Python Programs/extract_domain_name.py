
# question link : https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python 

# import library
import re

# url link
s = 'https://youtube.com'
s = 'https://123.net'
s = 'http://google.co.jp'
s = 'www.xakep.ru'

# # finding the protocol
# obj1 = re.findall('(\w+)://',s)
# print(obj1)

# # finding the hostname which may
# # contain dash or dots
# obj2 = re.findall('://www.([\w\-\.]+)',s)
# print(obj2)

pattern = '(www\.)?\w{1,3}?.\w+'
print(re.findall(pattern,s))

