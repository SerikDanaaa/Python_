n = int(input())  

def fib(n):              #WITH RECURSION
    if n ==1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2) + fib(n-3)

"""
fib1 = 1
fib2 = 1

while n-2 > 0:
    fib1,fib2 = fib2 , fib1+fib2
    n = n - 1
"""     
print(fib(n))    
