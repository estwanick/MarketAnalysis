#!/usr/bin/env python
import sys, math

ticker = None
month = None
year = None
cumulLinear = 0.0
cumulPoly = 0.0
cumulRBF = 0.0
cumulLM = 0.0

modelResults = {}
newMinValue = {}

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[2]
    cMonth = lineParams[1]

    actual = float(lineParams[3])
    
    linearScore = float(lineParams[4])
    polyScore = float(lineParams[5])
    rbfScore = float(lineParams[6])
    lmScore = float(lineParams[7])

    if (ticker == cTicker) and (year == cYear):
        cumulLinear = cumulLinear + (actual - linearScore)
        cumulPoly = cumulPoly + (actual - polyScore)
        cumulRBF = cumulRBF + (actual - rbfScore)
        cumulLM = cumulLM + (actual - lmScore)
    else:
        if ticker:
            cumulLinear = math.fabs(cumulLinear)
            cumulPoly = math.fabs(cumulPoly)
            cumulRBF = math.fabs(cumulRBF)
            cumulLM = math.fabs(cumulLM)
            modelResults['cumulLinear'] = cumulLinear
            modelResults['cumulPoly'] = cumulPoly
            modelResults['cumulRBF'] = cumulRBF
            modelResults['cumulLM'] = cumulLM
            
            newMinValue['value'] = 1000 #Assume worst case
            newMinValue['model'] = 'default'

            for key, value in modelResults.iteritems():
                if value < newMinValue['value']:
                    newMinValue['value'] = value
                    newMinValue['model'] = key

            print newMinValue['model'] + ': ' + str(newMinValue['value'])
            print '%s,%s,%s,%s,%s,%s,%s,%s'% (ticker, month, year, actual, cumulLinear, cumulPoly, cumulRBF, cumulLM)


        ticker = cTicker
        year = cYear
        month = cMonth
        cumulLinear = 0.0
        cumulPoly = 0.0
        cumulRBF = 0.0
        cumulLM = 0.0

if (ticker == cTicker) and (year == cYear):
    cumulLinear = math.fabs(cumulLinear)
    cumulPoly = math.fabs(cumulPoly)
    cumulRBF = math.fabs(cumulRBF)
    cumulLM = math.fabs(cumulLM)
    modelResults['cumulLinear'] = cumulLinear
    modelResults['cumulPoly'] = cumulPoly
    modelResults['cumulRBF'] = cumulRBF
    modelResults['cumulLM'] = cumulLM
    
    newMinValue['value'] = 1000 #Assume worst case
    newMinValue['model'] = 'default'

    for key, value in modelResults.iteritems():
        if value < newMinValue['value']:
            newMinValue['value'] = value
            newMinValue['model'] = key

    print newMinValue['model'] + ': ' + str(newMinValue['value'])
    print '%s,%s,%s,%s,%s,%s,%s,%s'% (ticker, month, year, actual, cumulLinear, cumulPoly, cumulRBF, cumulLM)
