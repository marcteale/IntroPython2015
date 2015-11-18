#!/usr/bin/python

def string_input(threedigit, twodecimalpointfloat, scientificnotation):
    # 'file_002 :   123.46, 1e+04'
    return "file_{:03d} :   {:06.2f}, {:.0e}".format(threedigit,twodecimalpointfloat,scientificnotation)

def print_first_three(*num):
    return "The first three numbers are: {}, {}, {}.".format(num[0], num[1], num[2])

def print_first_x(*num): # mine, shitty
    x = len(num)
    y = ''
    for i in num:
        y += str(i) + ", "
    return "The first {} numbers are: {}".format(x,y)

def instructors_version(*num): # also shitty, didn't get a chance to copy it.
    x = len(num)
    formatter= ", ".join(["{:d}" * len(num)])
    print('the first %i numbers are: {}').format(x,formatter)

print('file_002 :   123.46, 1e+04')
print(string_input(2,123.45678,10000))
print('')
print(print_first_three(3,5,23,45))
print(print_first_x(3,5,23,45))
print(instructors_version(3,5,23,45))
