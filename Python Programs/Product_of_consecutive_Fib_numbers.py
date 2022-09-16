
# question link : https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def productFib(prod):
    # generating fib sequence and checking prod in each iteration
    output = [0,1]
    while True:
        if output[-1]*output[-2] == prod:
            return [output[-2],output[-1],True]
        elif output[-1]*output[-2] > prod:
            return [output[-2],output[-1],False]
        else:
            output.append(sum(output[-2:]))
            
            
# solution 2 
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
            
print(productFib(44242))
