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

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    cClosingPrice = float(lineParams[4])

    if (ticker == cTicker) and (month == cMonth) and (year == cYear):
        dailyClosingPrices.append(cClosingPrice)
    else:
        if ticker:
            #print(dailyClosingPrices)\
            #return the monthly returns
            monthlyReturn = ( dailyClosingPrices[len(dailyClosingPrices) - 1] / dailyClosingPrices[0] ) - 1
            print '%s,%s,%s,%s' % (ticker, year, month, monthlyReturn)
            dailyClosingPrices = []

        ticker = cTicker
        year = cYear
        month = cMonth
        dailyClosingPrices.append(cClosingPrice)
        
# Just ignore last month for now
if (ticker == cTicker) and (month == cMonth) and (year == cYear):
    #print(dailyClosingPrices)
    monthlyReturn = ( dailyClosingPrices[len(dailyClosingPrices) - 1] / dailyClosingPrices[0] ) - 1
    print '%s,%s,%s,%s' % (ticker, year, month, monthlyReturn)