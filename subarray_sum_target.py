#Given a list of integers and a target number, list all pairs that sum up to that number  
def sub_array(arr, target):     
    # Initialize curr_sum as value of first element and starting point as 0 
    curr_sum = arr[0]
    start = 0
    n = len(arr)
 
    # Add elements one by one to curr_sum 
    # if the curr_sum > the sum, then remove 
    # starting element 
    i = 1
    while i <= n:
         
        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum and start < i-1:
         
            curr_sum = curr_sum - arr[start]
            start += 1
             
        # If curr_sum = sum, then return true
        if curr_sum == sum:
            print ("Sum found between indexes")
            print ("%d and %d"%(start, i-1))
            return True
 
        # Add this element to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
 
    # If we reach here, 
    # then no subarray
    print ("No subarray found")
    return False
 
# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23
 
sub_array(arr, sum)
 
# This code is Contributed by shreyanshi_arun.