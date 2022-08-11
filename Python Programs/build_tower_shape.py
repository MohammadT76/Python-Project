
# question link : 
# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
# ex) tower_builder(3), ['  *  ', ' *** ', '*****']

def tower_builder(n_floors):
    tower_list = []
    basic_element = '*'
    len_final_floor = (2*n_floors-1)*(len(basic_element))
    for floor in range(1,n_floors+1):
        tower_list.append(((2*(floor)-1)*basic_element).center(len_final_floor))
    return tower_list
    
    
print(tower_builder(4))