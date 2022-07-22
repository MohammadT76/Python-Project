
# this function getting a string , then remove all vowels characters from it 
# then return new_string

vowels = 'aAeEiIoOuU'

def disemvowel (string_):
    new_string = string_
    for char in vowels:
        new_string = new_string.replace(char,'')
    return new_string


string_ = "This website is for losers LOL!" 

print(disemvowel(string_))