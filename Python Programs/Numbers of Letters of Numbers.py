
# question link : https://www.codewars.com/kata/599febdc3f64cd21d8000117/train/python
# ex) numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]


def number_2_word(n):
    # for more information see this link : https://www.askpython.com/python/examples/convert-number-to-words
    
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    # If all the digits are encountered return blank string
    if(n==0):
        return ""
    else:
        # compute spelling for the last digit
        small_ans = arr[n%10]
        # keep computing for the previous digits and add the spelling for the last digit
        ans = number_2_word(int(n/10)) + small_ans + ""
    # Return the final answer
    return ans

def numbers_of_letters(n):
    temp = n
    li = []
    while True:
        num = number_2_word(temp)
        li.append(num)
        if len(li) > 1 or len(num) == temp:
            if len(num) == temp:
                return li
        temp = len(num)


# solution 2
NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def numbers_of_letters(n):
    s = ''.join(NUM[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])


print(numbers_of_letters(4001))