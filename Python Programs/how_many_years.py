# you can see the question in this link
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

# solution 1
def nb_year_v1 (p0, percent, aug, p):
    # parameters : p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
    # hint : population in
    
    # ensure that inputs p0 , aug and p is integer (these value can't be float)
    p0 = int(p0)
    aug = int(aug)
    p = int(p)
    
    needed_years = 0
    population = p0
    
    while True:       
        if percent is not None:
            population = population + int(population*(percent/100)) + aug
        else:
            population = population + aug
            
        needed_years += 1
            
        if population >= p:
            break           
    return needed_years
      
      
print(nb_year_v1(1500, 5, 100, 5000))  
print(nb_year_v1(1500000, None , 10000, 2000000))
print(nb_year_v1(1500000, 0.25, 1000, 2000000))



# solution 2
def nb_year_v2 (p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year_v2(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years

print(nb_year_v2(1500, 5, 100, 5000))  
# print(nb_year_v2(1500000, None , 10000, 2000000))
print(nb_year_v2(1500000, 0.25, 1000, 2000000))



# for more information , see this link :
# https://appdividend.com/2022/07/01/python-null/#:~:text=To%20check%20if%20a%20variable,are%20the%20very%20same%20object.
