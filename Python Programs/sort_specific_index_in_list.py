
# question link : 
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
# ex) [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
# for more information about sort , see these links : 
# https://docs.python.org/3/howto/sorting.html#:~:text=Key%20Functions,-Both%20list.&text=sort()%20and%20sorted(),element%20prior%20to%20making%20comparisons.&text=The%20value%20of%20the%20key,to%20use%20for%20sorting%20purposes.
# https://stackoverflow.com/questions/44461172/sort-the-odd-numbers-in-the-list

test = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def sort_array(source_array):
    # sorting odd numbers in source_array and convert list object to an iterator
    odds = iter(sorted(el for el in source_array if el % 2))
    # inserting sorted odds number in original soruce_array
    return [next(odds) if val%2 else val for val in source_array]

print(sort_array(test))