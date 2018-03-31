#Given an array of integers, 
#write an in-place function to bring all the non-zero elements to the left of the array keeping the original order.  

def move_zeros_right(arr):
    count = 0

    while arr.count(0) > 0 in arr:
        arr.remove(0)
        count += 1
    arr = arr + ([0] * count)
    return arr

A = [4,2,1,0,5,0,0,2]
print(move_zeros_right(A))

