#!/usr/bin/python


from string import maketrans


def rot13(instring):
    i = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    o = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    trantab = maketrans(i, o)
    return instring.translate(trantab)

if __name__ == '__main__':
    assert rot13('ab') == 'no'
    assert rot13('Zntargvp sebz bhgfvqr arne pbeare') == 'Magnetic from outside near corner'
