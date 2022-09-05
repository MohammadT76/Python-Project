
# question link : https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
# ex) wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(string):
    return [string[:index]+string[index].upper()+string[index+1:] for index in range(len(string)) if string[index] != ' ']


# solution 2 
def wave_v2 (str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


print(wave("ok ay"))