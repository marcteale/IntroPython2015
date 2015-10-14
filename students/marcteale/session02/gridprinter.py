#!/usr/bin/python

minus = '-'
plus  = '+'
space = ' '
bar   = '|'

def print_border(j):
    print(plus+space+((minus+space)*j)+plus+space+((minus+space)*j)+plus)

def print_lines(k,l):
    for i in range(0,k):
        print(bar + space*l + bar + space*l + bar)


def print_grid(n):
    a = n // 2
    b = (n - 2) // 2
    print_border(a)
    print_lines(b,n)
    print_border(a)
    print_lines(b,n)
    print_border(a)

print_grid(11)
print_grid(15)
print_grid(35)
