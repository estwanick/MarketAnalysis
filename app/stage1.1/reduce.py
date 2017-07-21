#!/usr/bin/env python

import sys
import numpy as np

ticker = None
closingPrice = None
month = None
year = None
stdDeviation = 0
#Hold daily prices for that month
dailyClosingPrices = []

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    cOpeningPrice = float(lineParams[4])
    cClosingPrice = float(lineParams[5])

    if (ticker == cTicker) and (month == cMonth) and (year == cYear):
        dailyClosingPrices.append(cClosingPrice)
    else:
        if ticker:
            #print(dailyClosingPrices)
            stdDeviation = np.std(dailyClosingPrices)
            print '%s,%s,%s,%s' % (ticker, year, month, stdDeviation)
            dailyClosingPrices = []

        ticker = cTicker
        year = cYear
        month = cMonth
        dailyClosingPrices.append(cClosingPrice)
        
# Just ignore last month for now
if (ticker == cTicker) and (month == cMonth) and (year == cYear):
    #print(dailyClosingPrices)
    stdDeviation = np.std(dailyClosingPrices)
    print '%s,%s,%s,%s' % (ticker, year, month, stdDeviation)
