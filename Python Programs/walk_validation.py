# question link in codewars:
# codewars.com/kata/54da539698b8a2ad76000228/train/python

test = ['n','n','n','s','n','s','n','s','n','s']
test = ['w','e','w','e','w','e','w','e','w']

# solution 1
def is_valid_walk_v1 (walk):
    x = 0
    y = 0
    for walking in walk:
        match walking:
            case 'n':
                y += 1
            case 's':
                y -= 1
            case 'e':
                x += 1
            case 'w':
                x -= 1
    return True if (x==0 and y==0 and len(walk) == 10) else False

print(is_valid_walk_v1(test))


# solution 2 
def is_valid_walk_v2 (walk):
        return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
    

print(is_valid_walk_v1(test))