#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
donors = [
    ['Bender Rodriguez', [50,100,150]],
    ['Phillip J. Fry', [20]],
    ['Turranga Leela', [25,27,1234]],
    ['Hubert J. Farnsworth', [1500,7]],
    ['Hermes Conrad', [200]],
    ['Zapp Brannigan', [5,10]],
    ['Amy Wong', [50000]]
]

#for donor,donations in donors:
#    print "Name: {}, donations {}".format(donor,donations)

def selection(*options):
    '''Takes a list of options, presents them to a user, and returns their selection as a string.'''
    while True:
        for i in range(len(options)):
            print "{}: {}".format(i,options[i])
        command = raw_input(': ')
        command = int(command)
        return options[command]

def get_donation():
    while True:
        amount = unicode(raw_input('Enter donation amount: '))
        if amount.isnumeric():
            return int(amount)
        else:
            print("That isn't a number.")


user_input = selection('Send a Thank You','Create a Report')

'''If the user (you) selects 'Send a Thank You', prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data structure and use it.
    If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn’t.
Once an amount has been given, add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.'''

if user_input == 'Send a Thank You':
    while True:
        user_input = raw_input('\nEnter full name: ')
        print user_input
        if user_input == 'list':
            print "Donors list:"
            for donor in donors: print(donor[0])
            continue
        for donor in donors:
            if donor == user_input:
                print('Donor found, adding to list of donations')
                donation = get_donation()
        else:
            # create new donor
            print('Not found, creating new record')
            new_donor = user_input
            donation = get_donation()
            donors.push([[donor],[donation]])

else:
    pass
