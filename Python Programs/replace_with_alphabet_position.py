
# question link : https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

import string

def alphabet_position(text):
    all_en_alphabet = string.ascii_lowercase
    alphabet_position = range(1,len(all_en_alphabet)+1)
    alphabet_dict = {all_en_alphabet[i]:alphabet_position[i] for i in range(len(all_en_alphabet)) }
    li_position = []
    for i in text.lower():
        if i in all_en_alphabet:
            li_position.append(alphabet_dict[i])
    return ' '.join(str(num) for num in li_position)


# solution 2
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(alphabet_position("The sunset sets at twelve o' clock."))
