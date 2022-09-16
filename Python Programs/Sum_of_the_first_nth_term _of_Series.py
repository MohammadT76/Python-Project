
# question link : https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
# usefull link : https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
#
# How can i limite floating point ? f'{a:.2f}' or round(14.22222223, 2)
#

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
def series_sum(n):
    result = 0
    for iter in range(n):
        result += 1/(1+iter*3)
    return str(f"{result:.2f}")

print(series_sum(1))