
# question link : 
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]

def longest_consec(strarr, k):
    if strarr is None or k > len(strarr):
        return ""
    else:
        li_str = []
        len_str = []
        for index in range(0,len(strarr)-k+1):
            string = ''
            for counter in range(k):
                string = string + ''.join(strarr[index+counter])
            li_str.append(string)
            len_str.append(len(string))
        return li_str[len_str.index(max(len_str))]

# checking for running time
import time
start_time = time.time()
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print("--- %s seconds ---" % (time.time() - start_time))


# solution 2
def longest_consec_v2 (strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result


# checking for running time
import time
start_time = time.time()
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print("--- %s seconds ---" % (time.time() - start_time))
