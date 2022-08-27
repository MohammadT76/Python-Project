
# question link : https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python

def rental_car_cost(d):
    return [40*d,40*d-20,40*d-50][int(d>=0)+int(d>=3)+int(d>=7)-1]

print(rental_car_cost(4))


# solution 2
def rental_car_cost_v2 (d):
    return [40*d,40*d-20,40*d-50][int(d>=0)+int(d>=3)+int(d>=7)-1]