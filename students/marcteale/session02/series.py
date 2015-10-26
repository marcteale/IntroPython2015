#!/usr/bin/python

def fibonacci(n):
    '''Return nth number in fibonacci sequence.'''
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    '''Return nth number in lucas sequence.'''
    if n == 0: return 2
    elif n == 1: return 1
    elif n == 2: return 3
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, n0 = 0, n1 = 1):
    '''Return nth number of sequence, where optional variables x and y are first two numbers in sequence.'''
    if n < 0: return None
    if n == 0: return n0
    if n == 1: return n1
    else:  
       return sum_series(n0 - 1) + sum_series(n1 - 1)


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13

assert lucas(0) == 2
assert lucas(1) == 1
assert lucas(4) == 7

#print sum_series(0)
#print sum_series(1)
#print sum_series(7)
print sum_series(0,2,1)
print sum_series(1,2,1)
print sum_series(2,2,1)
print sum_series(3,2,1)
print sum_series(4,2,1)
