#Determine if any 3 integers in an array sum to 0
#The following solutions assumes that repetitions 
#(i.e. choosing the same array element more than once) are *allowed*, 
#so the array [-5,1,10] contains a zero sum (-5-5+10) and so does [0] (0+0+0).
# e.g., [4, 2, -1, 1, -5, 6, -4] = True  

A = [4, 2, -1, 1, -5, 6, -4]
def sum_target_0(arr, target=0):
    if 0 in arr:
        return True

    arr.sort() 
 
    for i in range(0, len(arr)-2):
        l = i + 1
         
        # index of the last element
        r = len(arr)-1
        while (l < r):
            if( A[i] + A[l] + A[r] == target):
                print("Triplet is", A[i], 
                     ',', A[l], ',', A[r])
                return True
             
            elif (A[i] + A[l] + A[r] < target):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1
 
    # If we reach here, then
    # no triplet was found
    return False

print(sum_target_0(A))

#O(N**2)