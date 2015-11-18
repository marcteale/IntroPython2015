#!/usr/bin/python3.4


import ephem
from datetime import datetime
from datetime import timezone


def convert_to_datetime(ephemdate):
    return datetime.date(ephemdate.datetime())


def get_sunrise(place):
    sunrise = place.next_rising(sun)
    return convert_to_datetime(sunrise)

sun = ephem.Sun()
here = ephem.Observer()
here.lat = '47:36:34'
here.lon = '122:19:59'
here.pressure = 0
here.horizon = '-0:34'
here.date = datetime.today()
print(get_sunrise(here))
