#!/usr/bin/env python
import sys

cumulLinear = 0.0
cumulPoly = 0.0
cumulRBF = 0.0
cumulLM = 0.0


for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')
    month = lineParams[1]
    actual = float(lineParams[3])
    
    linearScore = float(lineParams[4])
    polyScore = float(lineParams[5])
    rbfScore = float(lineParams[6])
    lmScore = float(lineParams[7])

    cumulLinear = cumulLinear + (linearScore - actual)
    cumulPoly = cumulPoly + (polyScore - actual)
    cumulRBF = cumulRBF + (rbfScore - actual)
    cumulLM += cumulLM + (lmScore - actual)
    print '%s,%s,%s,%s,%s,%s,%s,%s'% (lineParams[0], lineParams[1], lineParams[2], actual, cumulLinear, cumulPoly, cumulRBF, cumulLM)
    