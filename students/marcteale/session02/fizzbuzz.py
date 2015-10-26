#!/usr/bin/python

for i in range(100):
    str=''
    if not (i % 3):
        str+='Fizz'
    if not (i % 5):
        str+='Buzz'
    if str == '':
        print(i)
    else:
        print(str)
