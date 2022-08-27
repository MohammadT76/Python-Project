
# question link : https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
# ex) test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])

def tribonacci(signature, n):
    if n <= 0:
        tribonacci_li = []
    elif 0 <= n <= len(signature):
        tribonacci_li = signature[0:n]
    else:
        tribonacci_li = signature.copy()
        for iter in range(1,(n-len(signature))+1):
            tribonacci_li.append(sum(tribonacci_li[iter-1:iter+3]))
    return tribonacci_li

print(tribonacci([3, 2, 1], 2))


# solution 2
def tribonacci_v2(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
