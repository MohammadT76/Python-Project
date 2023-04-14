
# question link : https://www.codewars.com/kata/6357825a00fba284e0189798/train/python

def get_sum(n):
    result = 0
    for r in range(n+1):
        for c in range(r,n+1):
            result += (2*r+c+1)
    return result


# solution 2
def get_sum(n):
    result = 0
    counter = n+1
    for i in range(n+1):
        temp = 2*i+i+1
        temp_2 = list(range(temp,temp+counter))
        result += sum(temp_2)
        counter -= 1
    return result


print(get_sum(3))
