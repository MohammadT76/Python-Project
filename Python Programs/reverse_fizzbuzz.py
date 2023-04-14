
# question link : https://www.codewars.com/kata/5a622f5f85bef7a9e90009e2/train/python

def reverse_fizzbuzz(string):
    rules = {
        'fizz' : 3,
        'buzz' : 5,
        'fizzbuzz' : 15
    }
    split_str = string.split()
    for iter in range(len(split_str)):
        if split_str[iter].lower() in rules.keys():
            split_str[iter] = -1
    return split_str



print(reverse_fizzbuzz("Fizz 688 689 FizzBuzz"))