
# question link : https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

def validate_pin(pin):
    try:
        return True if int(pin)>=0 and pin.isdigit() and (len(pin) == 4 or len(pin) == 6) else False
    except:
        return False
    
    
# solution 2
def validate_pin_v2 (pin):
    return len(pin) in (4, 6) and pin.isdigit()

    
# print(validate_pin_v2('0000'))
print(validate_pin_v2('1.232'))

# print(validate_pin('09876'))
# print(validate_pin('123'))
# print(validate_pin('+111'))

        