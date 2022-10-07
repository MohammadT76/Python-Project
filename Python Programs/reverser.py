
# question link : https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python

def reverse(number):
    digit_list = []
    while number>0:
        digit_list.append(number%10)
        number //= 10
    return sum(digit*10**(len(digit_list)-index-1) for index,digit in enumerate(digit_list))


# solution 2
def reverse(n):
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m

number = 4532
print(reverse(number))
