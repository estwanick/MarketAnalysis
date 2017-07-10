#!/usr/bin/env python
import sys, os, re

PATH = os.environ['mapreduce_map_input_file']
FILENAME = re.search('[^\/]+(\w+)$', PATH).group().replace('.csv', '')

idx = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(',')
    #Skip header row
    if idx != 0:
        print FILENAME + "," + row[0] + "," + row[4]
    idx = idx + 1
