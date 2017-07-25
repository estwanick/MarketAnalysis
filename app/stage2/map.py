#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')
    if int(lineParams[1]) > 2010 and int(lineParams[1]) < 2017:
        print '%s,%s,%s,%s'% (lineParams[0], lineParams[1], lineParams[2], lineParams[3])
    