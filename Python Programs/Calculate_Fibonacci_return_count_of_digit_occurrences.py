
def fib_digits(n):
    # generating fib sequence and checking prod in each iteration
    output = [0,1]
    for _ in range(n-1):
        output.append(sum(output[-2:]))
    return sorted([(str(output[-1]).count(str(digit)),digit) for digit in range(0,10) if str(output[-1]).count(str(digit)) != 0],
                  reverse=True)

# solution 2
from collections import Counter

def fib_digits(n):
    a, b = 0, 1
    for i in range(n): a, b = b, a+b
    return sorted(((b, int(a)) for a, b in Counter(str(a)).items()), reverse=True)

# desier result 
a = [(254, 3),(228, 2),(217, 6),(217, 0),(202, 5),(199, 1),(198, 7),(197, 8),(194, 4),(184, 9)]
print(a)

print(fib_digits(10000))