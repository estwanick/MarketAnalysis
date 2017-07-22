#!/usr/bin/env python

import sys
import numpy as np
from sklearn.svm import SVR
from sklearn import linear_model
ticker = None
closingPrice = None
month = None
year = None
stdDeviation = 0
linearVar = 0
polyVar = 0
rbfVar = 0

#Hold daily prices for that month
monthlyVolatilities = []
dates = []
for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    monthlyVolatility = lineParams[3]
    #initialize the svr objects for each model
    svrlin = SVR(kernel = 'linear', C=1e3)
    svrrbf = SVR(kernel = 'rbf', C=1000, gamma=10)
    svrpoly = SVR(kernel = 'poly', C=1000, gamma=10, max_iter=15, degree=3)
    lm = linear_model.LinearRegression()

    if (ticker == cTicker) and (month == cMonth):
        monthlyVolatilities.append(monthlyVolatility)
        dates.append(cYear)
    else:
        if ticker:
            dataX = np.array(dates).astype(np.float).reshape((len(dates),-1))
            dataY = np.array(monthlyVolatilities).astype(np.float)
            
            lm.fit(dataX, dataY)
            orgLm = lm.predict(2016)
            orgLmOutput = ('%s,%s,%s') % ('Original linear: ', orgLm, '; ')

            #fit the data for each model
            svrlin.fit(dataX, dataY)
            svrpoly.fit(dataX, dataY)
            svrrbf.fit(dataX, dataY)
            #calculate variance for each model
            linearVar = svrlin.predict(2016)
            polyVar = svrpoly.predict(2016)
            rbfVar = svrrbf.predict(2016)
            
            linearOutput = '%s%s%s' % ('linear: ', linearVar, '; ')
            polyOutput = '%s%s%s' % ('poly: ', polyVar, '; ')
            rbfOutput = '%s%s%s' % ('rbf: ', rbfVar, '; ')
            #harcode 2016 because that is what we are predicting
            print '%s,%s,%s,%s,%s,%s,%s' % (ticker, '2016', month, linearOutput, orgLmOutput, polyOutput, rbfOutput)
            monthlyVolatilities = []
            dates = []

        ticker = cTicker
        year = cYear
        month = cMonth
        monthlyVolatilities.append(monthlyVolatility)
        dates.append(cYear)

# Just ignore last month for now
if (ticker == cTicker) and (month == cMonth):
    dataX = np.array(dates).reshape((len(dates),-1))
    dataY = np.array(monthlyVolatilities)
            
    #fit the data for each model
    svrlin.fit(dataX, dataY)
    svrpoly.fit(dataX, dataY)
    svrrbf.fit(dataX, dataY)
    
    linearVar = svrlin.predict(2016)
    polyVar = svrpoly.predict(2016)
    rbfVar = svrrbf.predict(2016)
    
    linearOutput = '%s%s%s' % ('linear: ', linearVar, '; ')
    rbfOutput = '%s%s%s' % ('rbf: ', rbfVar, '; ')
    polyOutput = '%s%s%s' % ('poly: ', polyVar, '; ')
    #harcode 2016 because that is what we are predicting
    print '%s,%s,%s,%s,%s,%s' % (ticker, '2016', month, linearOutput, polyOutput, rbfOutput)
    
