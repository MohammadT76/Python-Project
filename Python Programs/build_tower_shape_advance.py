
# question link : 
# https://www.codewars.com/kata/57675f3dedc6f728ee000256

def tower_builder(n_floors, block_size):
    w, h = block_size
    tower_list = []
    basic_element = w*'*'
    len_final_floor = (2*n_floors-1)*(len(basic_element))
    for floor in range(1,n_floors+1):
        for _ in range(h):
            tower_list.append(((2*(floor)-1)*basic_element).center(len_final_floor))
    return tower_list

print(tower_builder(6,[2,1]))