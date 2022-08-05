
# question link in codewars : 
# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
# ex) dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

# how can i split a number to digits ? 
# https://www.delftstack.com/howto/python/split-integer-into-digits-python/

def dig_pow_v1 (n, p):
    digits = [int(n) for n in str(n)]
    digit_sum = sum(digits[i-p]**i for i in range(p,p+len(digits)))
    return -1 if (digit_sum%n) else int(digit_sum/n)

print(dig_pow_v1(695,2))
print(dig_pow_v1(46288, 3))


# solution 2
def dig_pow_v2 (n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

print(dig_pow_v1(46288, 3))