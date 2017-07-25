#!/usr/bin/env python
import sys

for line in sys.stdin:
<<<<<<< HEAD
    line = line.strip()
    lineParams = line.split(',')
    print '%s,%s,%s,%s,%s'% (lineParams[0], lineParams[1], lineParams[2], lineParams[3], lineParams[4])
=======
	line = line.strip()
	lineParams = line.split(',')
	print '%s,%s,%s,%s,%s'%(lineParams[0],lineParams[1],lineParams[2],lineParams[3],lineParams[4])
>>>>>>> 2d7c7e6d392a589353e75b3f8c7b7c0c344103c8
