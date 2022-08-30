
# question link : https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    return s[int(len(s)/2)-1:int(len(s)/2)+1] if ~len(s)%2 else s[int(len(s)/2)]
    
    
test = 'middle'
print(get_middle(test))


# solution 2
def get_middle_v2 (s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]