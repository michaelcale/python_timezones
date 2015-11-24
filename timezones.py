#!/usr/bin/python

from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %z"

server_time = datetime.now()
utc_time = datetime.now(timezone('UTC'))


def print_us_timezones():
    from pytz import all_timezones
    
    n = len(all_timezones)  # 559 total time zones
    for zone in all_timezones:
        if 'US' in zone:
            print zone


# print_us_timezones()


def convert_utc(utc_time, toTZ):
    return utc_time.astimezone(timezone(toTZ))


tm = convert_utc(utc_time, 'US/Pacific')
print tm.strftime(fmt)