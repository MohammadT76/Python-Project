
def incr_decr(lst,i):
    if isinstance(i,int):
        if i>=0:
            return [element+i for element in lst]
        else:
            return [element+i for element in lst]
    else:
        return 'i must be an integer number . please try again ...'

