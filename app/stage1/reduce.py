#!/usr/bin/env python

import sys
import numpy as np
from sklearn.svm import SVR
ticker = None
closingPrice = None
month = None
year = None
stdDeviation = 0
linearVar = 0
polyVar = 0
rbfVar = 0

#Hold daily prices for that month
dailyClosingPrices = []
dates = []
for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    cOpeningPrice = float(lineParams[4])
    cClosingPrice = float(lineParams[5])

    #initialize the svr objects for each model
    svrlin = SVR(kernel = 'linear', C=1e3)
    svrpoly = SVR(kernel = 'poly', C=1e3, degree = 2)
    svrrbf = SVR(kernel = 'rbf', C=1e3, gamma = 0.1)
    
    if (ticker == cTicker) and (month == cMonth) and (year == cYear):
        dailyClosingPrices.append(cClosingPrice)
        dates.append(cYear)
    else:
        if ticker:
            #print(dailyClosingPrices)
            #dates = np.reshape(dates, len(dates), 1)
            #fit the data for each model
            svrlin.fit(dates, dailyClosingPrices)
            svrpoly.fit(dates, dailyClosingPrices)
            svrrbf.fit(dates, dailyClosingPrices)
            #calculate variance for each model
            linearVar = svrlin.predict(dailyClosingPrices)
            polyVar = svrpoly.predict(dailyClosingPrices)
            rbfVar = svrrbf.predict(dailyClosingPrices)
            #create output strings for each
            linearOutput = 'linear: ' + linearVar + '; '
            polyOutput = 'poly: ' + polyVar + '; '
            rbfOutput = 'rbf: ' + rbfVar + '; '

            #stdDeviation = np.std(dailyClosingPrices)

            print '%s,%s,%s,%s,%s,%s' % (ticker, year, month, linearOutput, polyOutput, rbfOutput)
            dailyClosingPrices = []
            dates = []

        ticker = cTicker
        year = cYear
        month = cMonth
        dailyClosingPrices.append(cClosingPrice)
        
# Just ignore last month for now
if (ticker == cTicker) and (month == cMonth) and (year == cYear):
    #print(dailyClosingPrices)
    #stdDeviation = np.std(dailyClosingPrices)
    
    #fit the data for each model
    svrlin.fit(dates, dailyClosingPrices)
    svrpoly.fit(dates, dailyClosingPrices)
    svrrbf.fit(dates, dailyClosingPrices)
    #calculate variance for each model
    linearVar = svrlin.predict(dailyClosingPrices)
    polyVar = svrpoly.predict(dailyClosingPrices)
    rbfVar = svrrbf.predict(dailyClosingPrices)
    #create output strings for each
    linearOutput = 'linear: ' + linearVar + '; '
    polyOutput = 'poly: ' + polyVar + '; '
    rbfOutput = 'rbf: ' + '; '
    
    print '%s,%s,%s,%s,%s,%s' % (ticker, year, month, linearOutput, polyOutput, rbfOutput)
