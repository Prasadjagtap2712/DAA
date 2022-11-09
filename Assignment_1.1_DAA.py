''' Write a program non-recursive and recursive program to calculate 
Fibonacci numbers and analyze their time and space complexity'''

import time
# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
t1 = time.time()
n = int(input("Enter a number to find Fibonacci series using recursion: "))
print(fibonacci(n))
t2 = time.time()
recurr_time = t2-t1
print("Time for recursive fibonacci calculation is: ", recurr_time)
