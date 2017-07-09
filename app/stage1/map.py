#!/usr/bin/env python
import sys, os, re

PATH = os.environ['mapreduce_map_input_file']
FILENAME = re.search('[^\/]+(\w+)$', PATH).group().replace('.csv', '')

idx = 0
for line in sys.stdin:
    line = line.strip()
    if idx != 0:
        print FILENAME + "," + line
    idx = idx + 1
