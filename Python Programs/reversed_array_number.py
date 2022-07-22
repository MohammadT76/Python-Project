# this function get a number and reversed it . then seperate all digits and return 
# all of them in one list
# ex) 348597 => [7,9,5,8,4,3] , 0 => [0]

# solution 1
def digitize_v1 (input_number):
    # convert input_number to string using str() because of we want to use reversed function
    conv_in_num = reversed(str(input_number))
    return [int(n) for n in conv_in_num]

print(digitize_v1(0))


# solution 2
def digitize_v2 (input_number):
    return map(int, str(input_number)[::-1])

print(digitize_v2(0))

# for more information about this topic and tricks , see these links :
# https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/#:~:text=To%20convert%2C%20or%20cast%2C%20a,int(%22str%22)%20.
# https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/#:~:text=The%20most%20Pythonic%20way%20to,x)%20built%2Din%20function.


