
def expanded_form (num):
    li_num = []
    for index,value in enumerate(str(n)):
        li_num.append(int(value)*(10**(len(str(n))-1-index)))
    return ' + '.join(str(x) for x in li_num if x!=0)


# solution 2
def expanded_form_v2 (num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

# testing
n = 70304
print(expanded_form(n))
