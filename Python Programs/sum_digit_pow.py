
# question link : https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python
# about this question : Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

def sum_dig_pow(a, b):
    num_li = list(range(a,b+1))
    new_num_li = []
    for number in num_li:
        counter_pow = 0
        digit_pow = 0
        
        # for calculating power of a number 
        for digit in map(int,list(str(number))):
            counter_pow += 1
            digit_pow += digit**counter_pow
            
        if digit_pow == number:
            new_num_li.append(number)
    return new_num_li

# solution 2
def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]


print(sum_dig_pow(1,139))