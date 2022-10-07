
# question link : https://www.codewars.com/kata/53f17f5b59c3fcd589000390/train/python

class SecureList():
    temp = []

    def __init__(self,li):
        self.li = li

    def __str__(self):
        temp = self.li
        self.li = []
        return str(temp)


messages=SecureList([1,2,3,4])
print(messages)     # prints [1,2,3,4]
print(messages)     # prints []