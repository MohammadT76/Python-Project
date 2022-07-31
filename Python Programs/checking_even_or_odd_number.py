
# question link in codewars : 
# https://www.codewars.com/kata/555086d53eac039a2a000083/train/python

def lovefunc_v1 ( flower1, flower2 ):
    return True if (flower1%2 == 0 and flower2%2 != 0) or ((flower2%2 == 0 and flower1%2 != 0)) else False


print(lovefunc_v1(3,2))


# solution 2
def lovefunc_v2 ( flower1, flower2 ):
    return (flower1+flower2)%2

print(lovefunc_v2(3,2))
