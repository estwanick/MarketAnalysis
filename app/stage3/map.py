#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')
    print '%s,%s,%s,%s,%s,%s,%s,%s,'% (lineParams[0], lineParams[1], lineParams[2], lineParams[3], lineParams[4], lineParams[5], lineParams[6], lineParams[7])
    