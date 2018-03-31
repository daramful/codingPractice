#Write a program which stores the results of the numbers in a Fibonancci sequence in an array  
#The recruiter asked me to code a function that returns the Fibonacci sequence.  
import numpy as np

# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
 
def fib(n):
    fibonacci_numbers = [0, 1]
    for i in range(2,n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    return fibonacci_numbers

print(fib(9))
#O(n)