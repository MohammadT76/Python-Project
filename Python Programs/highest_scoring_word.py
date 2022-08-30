
def high(x):
    # generate all alphabet
    import string
    alphabet = list(string.ascii_lowercase)
    alphabet_score = range(1,len(alphabet)+1)
    dict_alphabet = {alphabet[i]:alphabet_score[i] for i in range(len(alphabet))}

    scoring_word = []
    x = x.split(' ')
    for word in x:
        scoring_word.append(sum(dict_alphabet[char] for char in word))
        
    return x[scoring_word.index(max(scoring_word))]
    
test = 'man i need a taxi up to ubud'
print(high(test))