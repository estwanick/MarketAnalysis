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
records2016 = []

for line in sys.stdin:
    line = line.strip()
    lineParams = line.replace('\t', ',').split(',')

    #Data conract
    #(ticker, month, '2015', actual2015, linearVar2015, polyVar2015, rbfVar2015, lmVar2015, actual2016, linearVar2016, polyVar2016, rbfVar2016, lmVar2016)

    cTicker = lineParams[0]
    cYear = lineParams[2]
    cMonth = lineParams[1]

    actual = float(lineParams[3])
    
    linearScore = float(lineParams[4])
    polyScore = float(lineParams[5])
    rbfScore = float(lineParams[6])
    lmScore = float(lineParams[7])

    actual2016 =  float(lineParams[8])
    linearScore2016 = float(lineParams[9])
    polyScore2016 = float(lineParams[10])
    rbfScore2016 = float(lineParams[11])
    lmScore2016 = float(lineParams[12])
    
    if ticker == cTicker:
        cumulLinear = cumulLinear + (actual - linearScore)
        cumulPoly = cumulPoly + (actual - polyScore)
        cumulRBF = cumulRBF + (actual - rbfScore)
        cumulLM = cumulLM + (actual - lmScore)
        recline = '%s,%s,%s,%s,%s'%(actual2016, linearScore2016, polyScore2016, rbfScore2016, lmScore2016)
        records2016.append(recline)
    else:
        if ticker or ticker == None:
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

            mostAccurateModel2015 = newMinValue['model']
            mostAccurateModelvalue2015 = newMinValue['value']
            predictionFor2016 = 1000 #Assume worst case
            #Fetch the corresponding model for 2016
            if(mostAccurateModel2015 == 'cumulLinear'):
                predictionFor2016 = linearScore2016
            elif(mostAccurateModel2015 == 'cumulPoly'):
                predictionFor2016 = polyScore2016
            elif(mostAccurateModel2015 == 'cumulRBF'):
                predictionFor2016 = rbfScore2016
            elif(mostAccurateModel2015 == 'cumulLM'):
                predictionFor2016 = lmScore2016
            else:
                predictionFor2016 = "***ERROR***"

            #print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'% (ticker, '2015', actual, mostAccurateModel2015, mostAccurateModelvalue2015, '2016', actual2016, predictionFor2016, 'Accuracy:', actual2016 - predictionFor2016)

            counter2016 = 0
            for line2016 in records2016:
                counter2016 = counter2016 + 1
                splitLine = line2016.split(',')
                if(mostAccurateModel2015 == 'cumulLinear'):
                    pred2016 = splitLine[1]
                elif(mostAccurateModel2015 == 'cumulPoly'):
                    pred2016 = splitLine[2]
                elif(mostAccurateModel2015 == 'cumulRBF'):
                    pred2016 = splitLine[3]
                elif(mostAccurateModel2015 == 'cumulLM'):
                    pred = splitLine[4]
                else:
                    predictionFor2016 = "***ERROR***"
                actual16 = splitLine[0]
                if(predictionFor2016 != "***ERROR***"):
                    #ticker, year, month, actual, prediction, residual
                    print '%s,%s,%s,%s,%s,%s'%(ticker, '2016', counter2016, actual16, pred2016, str(float(actual16)  - float(pred2016)))
                else:
                    print '%s,%s,%s'%('2016', counter2016, "***Error***")
            records2016 = []
            records2016.append('%s,%s,%s,%s,%s'%(actual2016, linearScore2016, polyScore2016, rbfScore2016, lmScore2016))

        ticker = cTicker
        year = cYear
        month = cMonth
        cumulLinear = 0.0
        cumulPoly = 0.0
        cumulRBF = 0.0
        cumulLM = 0.0

if (ticker == cTicker):
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

    mostAccurateModel2015 = newMinValue['model']
    mostAccurateModelvalue2015 = newMinValue['value']
    predictionFor2016 = 1000 #Assume worst case
    #Fetch the corresponding model for 2016
    if(mostAccurateModel2015 == 'cumulLinear'):
        predictionFor2016 = linearScore2016
    elif(mostAccurateModel2015 == 'cumulPoly'):
        predictionFor2016 = polyScore2016
    elif(mostAccurateModel2015 == 'cumulRBF'):
        predictionFor2016 = rbfScore2016
    elif(mostAccurateModel2015 == 'cumulLM'):
        predictionFor2016 = lmScore2016
    else:
        predictionFor2016 = "***ERROR***"

    #print '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s'% (ticker, '2015', actual, mostAccurateModel2015, mostAccurateModelvalue2015, '2016', actual2016, predictionFor2016, 'Accuracy:', actual2016 - predictionFor2016)

    counter2016 = 13
    for line2016 in records2016:
        counter2016 = counter2016 - 1
        splitLine = line2016.split(',')
        if(mostAccurateModel2015 == 'cumulLinear'):
            pred2016 = splitLine[1]
        elif(mostAccurateModel2015 == 'cumulPoly'):
            pred2016 = splitLine[2]
        elif(mostAccurateModel2015 == 'cumulRBF'):
            pred2016 = splitLine[3]
        elif(mostAccurateModel2015 == 'cumulLM'):
            pred = splitLine[4]
        else:
            predictionFor2016 = "***ERROR***"
        actual16 = splitLine[0]
        if(predictionFor2016 != "***ERROR***"):
            print '%s,%s,%s,%s,%s,%s'%(ticker, '2016', counter2016, actual16, pred2016, str(float(actual16)  - float(pred2016)))
        else:
            print '%s,%s,%s'%('2016', counter2016, "***Error***")
    records2016 = []
    records2016.append('%s,%s,%s,%s,%s'%(actual2016, linearScore2016, polyScore2016, rbfScore2016, lmScore2016))
