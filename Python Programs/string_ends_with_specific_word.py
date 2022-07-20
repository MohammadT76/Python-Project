
# example : solution('abc', 'bc') --> return true

# solution 1
def check_str_v1 (string,pattern):
    patter_size = len(pattern)
    if patter_size == 0:
        return True
    else:
        string_pattern = string[-patter_size:]
        return string_pattern.lower() == pattern.lower()
    
print(check_str_v1('abBC','bc'))


# solution 2
# this function is sensitive to lower or uppers case words
def check_str_v2 (string,pattern):
    return string.endswith(pattern)
    # if you want check multi pattern , test this line:
    # 'hello'.endswith(('loo','lo','loooo'))

print(check_str_v2('abc','bc'))
