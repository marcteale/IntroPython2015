#!/usr/bin/python


def one(str):
    '''Return a sequence with the first and last items exchanged.'''
    # return str[-1] + str[1:-1] + str[0] # Mine
    return str[-1:] + str[1:-1] + str[:1]  # Adding colons makes the returned
    # value a sequence, so it works with non-string values


def two(str):
    '''Return a sequence with every other item removed.'''
    # return str[0:-1:2] # Mine
    return str[:-1:2]  # The first zero is assumed.


def three(str):
    '''Return a sequence with the first and last 4 items removed, and every other
    item in between.'''
    return str[4:-4:2]  # Yay, I got one.


def four(str):
    '''Return a sequence reversed (just with slicing).'''
    return str[::-1]  # I don't get it.


def five(str):
    '''Return a sequence with the middle third, then last third, then the first
    third in the new order.'''
    x = len(str) // 3
    return str[x:x*2] + str[x*2:x*3] + str[:x]  # Mine

print(one('blag'))
print(two('Bob sucks.'))
print(three('asdfaabbccddasdf'))
print(four('abcdef'))
print(five('thisthatbluh'))
