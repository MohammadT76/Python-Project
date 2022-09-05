

def first_non_consecutive(arr):
    if len(arr) == 1 or len(arr) == 0:
        return None
    else:
        for i in range(len(arr)-2):
            if arr[i+2]-arr[i+1] > arr[i+1]-arr[i]:
                return arr[i+2]
            elif arr[i+2]-arr[i+1] < arr[i+1]-arr[i]:   
                return arr[i+1]
            else:
                continue 
    

# solution 2
def first_non_consecutive_v2 (a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None
    
test = [4,5,6,8,9,11]
print(first_non_consecutive_v2(test))