
# question link : https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
# usefull link : https://stackoverflow.com/questions/38273353/how-to-repeat-individual-characters-in-strings-in-python

def double_char(s):
    # Number of repetitions of each letter
    n = 2
    return ''.join(char*n for char in s)


test = "1234!_ "
print(double_char(test))