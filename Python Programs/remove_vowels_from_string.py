
# this function getting a string , then remove all vowels characters from it 
# then return new_string

# solution 1
vowels = 'aAeEiIoOuU'

def disemvowel_v1 (string_):
    new_string = string_
    for char in vowels:
        new_string = new_string.replace(char,'')
    return new_string


string_ = "This website is for losers LOL!" 

print(disemvowel_v1(string_))


# solution 2
def disemvowel_v2 (string):
    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel_v2(string_))