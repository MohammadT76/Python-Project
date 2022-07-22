# this function getting an string an reverse each word that exist in 
# string , then return it

a = 'This is an example!'
b = "double  spaces"
c = 'double        spaced     words'

def reverse_words(a):
    word_list = a.split(' ')
    reverse_word_list = [revers_word[::-1] for revers_word in word_list]
    reverse_str = ' '.join(reverse_word_list)
    return reverse_str
    
    
print(reverse_words(c))
    
    

# for more information or see similar topics , see these links : 
# https://stackoverflow.com/questions/34460588/count-the-number-of-spaces-between-words-in-a-string
# https://www.geeksforgeeks.org/python-reverse-word-sentence/

