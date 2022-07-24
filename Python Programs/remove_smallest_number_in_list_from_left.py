
def remove_smallest(numbers):
    new_numbers = numbers
    try:
        new_numbers.remove(min(new_numbers))
    except:
        new_numbers = []
    return new_numbers


print(remove_smallest([1,2,3,4,5]))