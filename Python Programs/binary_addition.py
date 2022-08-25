
# convert to binary 
binary = bin(19)
print(binary)
print(len(binary))
print('################')

# print without 0b...
bindata = format(19, "b")
print(bindata)
print(type(bindata))

# for more information see this link : 
# https://appdividend.com/2021/06/14/how-to-convert-python-int-to-binary-string/#:~:text=To%20convert%20int%20to%20binary%20in%20Python%2C%20use%20the%20bin,string%20prefixed%20with%20%E2%80%9C0b%E2%80%9D.

####################################
# question link : https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python

def add_binary(a,b):
    return format(a+b,'b')

# print(add_binary(0,1))
print(add_binary(2,2))