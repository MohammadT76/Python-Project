
s = 'this is a test for this function'
s = 'hello world .'

# solution 1
def find_short_v1 (s):
    word_list = s.split()
    try:
        word_list.remove('.')
    except:
        pass
    word_len = [len(length_word) for length_word in word_list]
    return min(word_len)
    
print(find_short_v1(s))


# solution 2
def find_short_v2 (s):
    return min(map(len, s.split(' ')))

print(find_short_v2(s))


# for more information you can see this link :
# https://thispointer.com/python-how-to-remove-multiple-elements-from-list/#:~:text=Remove%20Multiple%20elements%20from%20list%20by%20index%20range%20using%20del,can%20use%20del%20keyword%20i.e.&text=It%20will%20delete%20the%20elements,from%20index1%20to%20index2%20%E2%80%93%201.
