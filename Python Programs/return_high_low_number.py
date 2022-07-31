
from cgi import print_arguments


test = "1 2 3 4 5"

def high_and_low (numbers):
    # convert string to integers
    num_list = [int(n) for n in numbers.split()]
    return f"{max(num_list)} {min(num_list)}"


print(high_and_low(test))