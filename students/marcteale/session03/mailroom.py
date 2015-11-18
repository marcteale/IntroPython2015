from textwrap import dedent

donors = [
    (['Bender Rodriguez', [50, 100, 150]]),
    (['Phillip J. Fry', [20]]),
    (['Turranga Leela', [25, 2, 1234]]),
    (['Hubert J. Farnsworth', [1500, 7]]),
    (['Hermes Conrad', [200]]),
    (['Zapp Brannigan', [5, 10]]),
    (['Amy Wong', [50000]])
]


def main_menu_selection():
    print('\n1: Print thank you')
    print('2: Generate report')
    print('3: Exit')
    action = input(':')
    return action.strip()


def get_name():
    return input('\nEnter name of donor, or LIST for all donors: ').strip()


def find_donor(name):
    for donor in donors:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None


def add_donation(name):
    # TODO: Only adds a new donation, doesn't append to existing
    getting_donation = True
    while getting_donation:
        donation = input('Enter donation amount: ').strip()
        if donation.isnumeric():
            name = (name, float(donation))
            getting_donation = False
        else:
            print('Donation amount was not a number.')
    return


def add_donor(name):
    print('\nAdding new donor.')
    name = (name, [])
    donors.append(name)
    return


def print_donor_list():
    for donor in donors:
        print(donor[0])
    return


def send_thank_you():
    name = get_name()
    if name == 'LIST':
        print_donor_list()
    elif not find_donor(name):  # Add donor if not in DB
        add_donor(name)
    add_donation(name)
    print(print_thank_you(name))


def print_thank_you(name):
    return dedent('''
        Dear {},

        Thank you kindly for your donations totalling {}.  They will be used
        in the continued efforts to eradicate the human race.

        Sincerely
        Morbo the Annihilator
        ''').format(donors[0], donors[1][-1])


def generate_report():
    print('generate report')


if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu_selection()
        if selection == '1':
            send_thank_you()
        elif selection == '2':
            generate_report()
        elif selection == '3':
            running = False
        else:
            print('The fuck is wrong with you?  Pick one of the numbers.\n')
