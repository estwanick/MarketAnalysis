#!/usr/bin/env python

import sys
import numpy as np
from sklearn.svm import SVR
from sklearn import linear_model
#import matplotlib.pyplot as plt

ticker = None
closingPrice = None
month = None
year = None
stdDeviation = 0
linearVar = 0
polyVar = 0
rbfVar = 0

#Hold daily prices for that month
monthlyReturns = []
dates = []
for line in sys.stdin:
    line = line.strip()
    lineParams = line.replace('\t', ',').split(',')

    cTicker = lineParams[0]
    cYear = lineParams[2]
    cMonth = lineParams[1]
    monthlyReturn = lineParams[3]
    #initialize the svr objects for each model
    svrlin = SVR(kernel = 'linear', C=1e3)
    svrrbf = SVR(kernel = 'rbf', C=1e3, gamma=10)
    svrpoly = SVR(kernel = 'poly', C=1e3, gamma=10, max_iter=15, degree=2)
    #svrlin2 = SVR(kernel = 'linear', C=1e3)
    #svrrbf2 = SVR(kernel = 'rbf', C=1e3, gamma=10)
    #svrpoly2 = SVR(kernel = 'poly', C=1e3, gamma=10, max_iter=15, degree=2)
    lm = linear_model.LinearRegression()
    #lm2 = linear_model.LinearRegression()

    if (ticker == cTicker) and (month == cMonth):
        monthlyReturns.append(monthlyReturn)
        dates.append(cYear)
        #print '%s,%s,%s,%s' % (cTicker, cYear, cMonth, monthlyReturn)
    else:
        if ticker:
            returnsMinusLast2 = monthlyReturns[ 0 : len(monthlyReturns)-2]
            datesWithoutLast2 = dates[ 0 : len(dates)-2]
            returnsWithout2016 = monthlyReturns[ 0 : len(monthlyReturns)-1]
            datesWithout2016 = dates [ 0 : len(dates) -1]
            dataX = np.array(datesWithout2016).reshape((len(datesWithout2016),-1))
            dataY = np.array(returnsWithout2016).astype(np.float)
            dataX2 = np.array(datesWithoutLast2).reshape((len(datesWithoutLast2),-1))
            dataY2 = np.array(returnsMinusLast2).astype(np.float)
            #fit the data for each model
            svrlin.fit(dataX, dataY)
            svrpoly.fit(dataX, dataY)
            svrrbf.fit(dataX, dataY)
            lm.fit(dataX, dataY)
            #calculate variance for each model
            linearVar2016 = svrlin.predict(2016)[0]
            polyVar2016 = svrpoly.predict(2016)[0]
            rbfVar2016 = svrrbf.predict(2016)[0]
            lmVar2016 = lm.predict(2016)[0]

            svrlin.fit(dataX2, dataY2)
            svrpoly.fit(dataX2, dataY2)
            svrrbf.fit(dataX2, dataY2)
            lm.fit(dataX2, dataY2)
            #calculate variance for each model
            linearVar2015 = svrlin.predict(2015)[0]
            polyVar2015 = svrpoly.predict(2015)[0]
            rbfVar2015 = svrrbf.predict(2015)[0]
            lmVar2015 = lm.predict(2015)[0]

            #linearOutput = '%s%s%s' % ('linear: ', linearVar, '; ')
            #polyOutput = '%s%s%s' % ('poly: ', polyVar, '; ')
            #rbfOutput = '%s%s%s' % ('rbf: ', rbfVar, '; ')
            actual2016 = monthlyReturns[len(monthlyReturns) -1]
            actual2015 = monthlyReturns[len(monthlyReturns) -2]
            print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (ticker, month, '2015', actual2015, linearVar2015, polyVar2015, rbfVar2015, lmVar2015, actual2016, linearVar2016, polyVar2016, rbfVar2016, lmVar2016)


        ticker = cTicker
        year = cYear
        month = cMonth
        monthlyReturns.append(monthlyReturn)
        dates.append(cYear)

# Just ignore last month for now
if (ticker == cTicker) and (month == cMonth):
    returnsMinusLast2 = monthlyReturns[ 0 : len(monthlyReturns)-2]
    datesWithoutLast2 = dates[ 0 : len(dates)-2]
    returnsWithout2016 = monthlyReturns[ 0 : len(monthlyReturns)-1]
    datesWithout2016 = dates [ 0 : len(dates) -1]
    dataX = np.array(datesWithout2016).reshape((len(datesWithout2016),-1))
    dataY = np.array(returnsWithout2016).astype(np.float)
    dataX2 = np.array(datesWithoutLast2).reshape((len(datesWithoutLast2),-1))
    dataY2 = np.array(returnsMinusLast2).astype(np.float)
    #fit the data for each model
    svrlin.fit(dataX, dataY)
    svrpoly.fit(dataX, dataY)
    svrrbf.fit(dataX, dataY)
    lm.fit(dataX, dataY)
    #calculate variance for each model
    linearVar2016 = svrlin.predict(2016)[0]
    polyVar2016 = svrpoly.predict(2016)[0]
    rbfVar2016 = svrrbf.predict(2016)[0]
    lmVar2016 = lm.predict(2016)[0]

    svrlin.fit(dataX2, dataY2)
    svrpoly.fit(dataX2, dataY2)
    svrrbf.fit(dataX2, dataY2)
    lm.fit(dataX2, dataY2)
    #calculate variance for each model
    linearVar2015 = svrlin.predict(2015)[0]
    polyVar2015 = svrpoly.predict(2015)[0]
    rbfVar2015 = svrrbf.predict(2015)[0]
    lmVar2015 = lm.predict(2015)[0]

    #linearOutput = '%s%s%s' % ('linear: ', linearVar, '; ')
    #polyOutput = '%s%s%s' % ('poly: ', polyVar, '; ')
    #rbfOutput = '%s%s%s' % ('rbf: ', rbfVar, '; ')
    actual2016 = monthlyReturns[len(monthlyReturns) -1]
    actual2015 = monthlyReturns[len(monthlyReturns) -2]
    print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (ticker, month, '2015', actual2015, linearVar2015, polyVar2015, rbfVar2015, lmVar2015, actual2016, linearVar2016, polyVar2016, rbfVar2016, lmVar2016)

