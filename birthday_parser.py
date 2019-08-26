#!/usr/bin/env python

import re
import csv
from datetime import date

today = date.today()
data = open('facebook_html.txt', 'r').read()

matched_data = re.findall(r'data-tooltip-content="(?P<name>[a-z0-9 ]+)\((?P<month>\d{1,2})\/(?P<day>\d{1,2})\)"', data, re.IGNORECASE)

with open('birthdays.csv', 'w') as csvfile:
    headers = ['Subject', 'Start date', 'All Day Event']
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(headers)
    for row in matched_data:
        day = int(row[2])
        month = int(row[1])

        if month <= today.month and day < today.day:
            year = today.year + 1
        else:
            year = today.year

        writer.writerow([row[0], f"{day}/{month}/{year}", True])
