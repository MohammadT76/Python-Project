
# question link : https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python

def Xbonacci(signature,n):
    if n <= 0:
        tribonacci_li = []
    elif 0 <= n <= len(signature):
        tribonacci_li = signature[:n]
    else:
        tribonacci_li = signature.copy()
        for iter in range(1,(n-len(signature))+1):
            tribonacci_li.append(sum(tribonacci_li[iter-1:iter+len(signature)]))
    return tribonacci_li

print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))
print(len(Xbonacci([1,0,0,0,0,0,0,0,0,0],20)))

#%%
# solution 2
def Xbonacci(signature,n):
    output, x = signature[:n], len(signature)
    while len(output) < n:
        output.append(sum(output[-x:]))
    return output

print(len(Xbonacci([1,0,0,0,0,0,0,0,0,0],20)))

# %%
