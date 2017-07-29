#!/usr/bin/env python

import sys
import numpy as np

ticker = None
closingPrice = None
month = None
year = None
monthlyReturn = 0
#Hold daily prices for that month
dailyClosingPrices = []
unsortedDays = {}

for line in sys.stdin:
    line = line.strip()
    lineParams = line.replace('\t', ',').split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    cClosingPrice = float(lineParams[4])
    cDay = lineParams[3]

    # print '%s,%s,%s,%s' % (ticker, year, month, cDay)
    if (ticker == cTicker) and (month == cMonth) and (year == cYear):
        #dailyClosingPrices.append(cClosingPrice)
        unsortedDays[int(cDay)] = cClosingPrice
    else:
        if ticker:
            for key in unsortedDays:
                dailyClosingPrices.append(unsortedDays[key])
            #return the monthly returns
            monthlyReturn = ( dailyClosingPrices[len(dailyClosingPrices) - 1] / dailyClosingPrices[0] ) - 1
            print '%s,%s,%s,%s' % (ticker, year, month, monthlyReturn)
            dailyClosingPrices = []
            unsortedDays = {}

        ticker = cTicker
        year = cYear
        month = cMonth
        unsortedDays[int(cDay)] = cClosingPrice
        
if (ticker == cTicker) and (month == cMonth) and (year == cYear):
    for key in unsortedDays:
                dailyClosingPrices.append(unsortedDays[key])
    monthlyReturn = ( dailyClosingPrices[len(dailyClosingPrices) - 1] / dailyClosingPrices[0] ) - 1
    print '%s,%s,%s,%s' % (ticker, year, month, monthlyReturn)
