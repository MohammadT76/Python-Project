
# question link : https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncing_ball(h, bounce, window):
    count_see = 1
    if (h>0) and (0<bounce<1) and (window<h):
        rebounce = h
        while rebounce > window:
            rebounce = rebounce*bounce
            if rebounce > window:
                count_see += 2
        return count_see
    return -1

# print(bouncing_ball(3, 0.66, 1.5))
# print(bouncing_ball(30, 0.66, 1.5))
# print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(30, 0.75, 1.5))