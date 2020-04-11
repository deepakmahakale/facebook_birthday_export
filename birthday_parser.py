#!/usr/bin/env python

import re
import csv
from datetime import date
import datetime

today = date.today()
presentDayOfWeek = int(today.strftime("%w"))
data = open('facebook_html.txt', 'r').read()

week   = ['Sunday', 
          'Monday', 
          'Tuesday', 
          'Wednesday', 
          'Thursday',  
          'Friday', 
          'Saturday']

matched_data = re.findall(r'data-tooltip-content="(?P<name>[a-z0-9 ]+)\((?P<month>\d{1,2})\/(?P<day>\d{1,2})\)"', data, re.IGNORECASE)
matched_data2 = re.findall(r'data-tooltip-content="(?P<name>[a-z0-9 ]+)\((?P<day>[a-z]+)\)"', data, re.IGNORECASE)

with open('birthdays.csv', 'w') as csvfile:
    headers = ['Subject', 'Start date', 'All Day Event']
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow(headers)
    for row in matched_data:
        day = int(row[2])
        month = int(row[1])

        if month < today.month or (month == today.month and day < today.day):
            year = today.year + 1
        else:
            year = today.year

        writer.writerow([row[0], f"{day}/{month}/{year}", True])
    for row in matched_data2:
        dayOfWeek = week.index(row[1])

        if dayOfWeek > presentDayOfWeek:
            delta = dayOfWeek-presentDayOfWeek
            newDate = today + datetime.timedelta(days=delta)
        else:
            delta = 7 + dayOfWeek-presentDayOfWeek
            newDate = today + datetime.timedelta(days=delta)

        writer.writerow([row[0], f"{newDate.day}/{newDate.month}/{newDate.year}", True])