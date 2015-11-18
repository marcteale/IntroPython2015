#!/usr/bin/python


def safe_input(prompt):
    try:
        userdata = raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return userdata

print(safe_input('Enter something: '))
