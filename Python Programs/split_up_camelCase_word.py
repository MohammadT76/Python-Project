
# question link : https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
# for more information see these links : 
# https://stackoverflow.com/questions/5020906/python-convert-camel-case-to-space-delimited-using-regex-and-taking-acronyms-in
# https://stackoverflow.com/questions/24385114/what-does-this-regular-expression-mean-a-z1a-z0-9-3-13
# https://www.regular-expressions.info/lookaround.html

import re
def solution(s):
    return re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', s)


# solution 2
def solution(s):
    return re.sub("([a-z])([A-Z])","\g<1> \g<2>",s)


# solution 3
def solution(s):
    return ''.join(char if char.islower() else ' '+char for char in s)

print(solution('camelCaseOkay'))