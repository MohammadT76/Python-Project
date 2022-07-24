
test = 'hello to 1213 .'
test = "45385593107843568"

# solution 1
def fake_bin_v1 (x):
    
    test_list = [n for n in x]
    test_list_fake = []
    
    for num in test_list:
        if int(num) >= 5:
            test_list_fake.append('1')
        else:
            test_list_fake.append('0')
    fake_string = ''.join(test_list_fake)
    
    return fake_string


print(fake_bin_v1(test))



# solution 2
def fake_bin_v2 (x):
    return ''.join('1' if int(char)>=5 else '0' for char in x)

print(fake_bin_v2(test))