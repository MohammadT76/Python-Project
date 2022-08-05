 
# question link : 
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# ex) find_nb (1071225) --> 45
# useful link : 
# https://math.stackexchange.com/questions/294213/prove-that-13-23-n3-1-2-n2

def find_nb(m):
    result = 0
    n = 1
    while True:
        result = result + pow(n,3)
        # result = lambda n : (pow(n,2)*pow(n+1,2))/4
        if result == m:
            return n
        elif result != m:
            n += 1
        elif result > m:
            n = -1
            break
    return -1
    
print(find_nb(2472962))    