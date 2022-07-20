
string = 'hello'

# solution 1
def reverse_str_v1 (string):
    return string[::-1]

print(reverse_str_v1(string))


# solution 2
def reverse_str_v2 (string):
    # convert string to reversed iterable
    string = reversed(string)
    return ''.join(string)

print(reverse_str_v2(string))


# for more information see this link:
# https://dbader.org/blog/python-reverse-string