#!/usr/bin/env python

import requests
import sys
from IPython import embed

urldata = requests.get(
    "http://api.wunderground.com/api/9394e65e04847b41/hourly/q/OH/Dayton.json")
data = urldata.json()

headers_to_print = [
    'time',
    'fctcode',
    'sky',
    'snow',
    'wx',
    'humidity',
    'uvi',
    'pop',
    'condition',
    'temp',
    ]
rows = []
for day in data['hourly_forecast']:
    # print(day)
    row = []

    if int(day['FCTTIME']['hour_padded']) in [6, 7, 8, 13, 14, 15]:
        row.append(day['FCTTIME']['civil'])
        for header in headers_to_print:
            if header not in day:
                continue
            types_to_add = [str, int]
            if sys.version_info.major == 2:
                types_to_add.append(unicode)
            if type(day[header]) in types_to_add:
                row.append(day[header])
            if 'english' in day[header]:
                row.append(day[header]['english'])
            else:
                pass
            rows.append(row)
temperature = [
    rows[0][9],
    rows[1][9],
    rows[2][9],
    rows[3][9],
    rows[4][9],
    rows[6][9]]
temperatures = [int(i) for i in temperature]
percentrai = [
    rows[0][7],
    rows[1][7],
    rows[2][7],
    rows[3][7],
    rows[4][7],
    rows[6][7]]
percentrain = [int(i) for i in percentrai]
condition = [
    rows[0][8],
    rows[1][8],
    rows[2][8],
    rows[3][8],
    rows[4][8],
    rows[6][8]]
conditionohshit = [
        "Snow",
        "Rain",
        "Rain/Wind",
        "Showers",
        "Showers/Wind",
        "Chance of Rain",
        "Freezing Rain",
        "Hail Showers",
        "Thunderstorms",
        "Thunderstorm"]
if min(temperatures) > 49:
    tempcheck = True
else:
    tempcheck = False

if max(percentrain) < 25:
    raincheck = True
else:
    raincheck = False

if str(conditionohshit) in condition:
    conditioncheck = False
else:
    conditioncheck = True

if tempcheck and raincheck and conditioncheck:
    print("Ride your motorcycle to work today, you silly bitch.")
else:
    print("Oh hell no. You're going to be cold or wet or something you pansy ass fuckboi")
