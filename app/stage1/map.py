#!/usr/bin/env python
import sys, os, re
from datetime import datetime

PATH = os.environ['mapreduce_map_input_file']
FILENAME = re.search('[^\/]+(\w+)$', PATH).group().replace('.csv', '')

EXCLUDE_YEARS = ['2017']

idx = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(',')
    #Skip header row
    if idx != 0:
        rowDate = datetime.strptime(str(row[0]), '%Y-%m-%d')
        rowYear = str(rowDate.year)
        rowMonth = str(rowDate.month)
        rowDay = str(rowDate.day)
        closingPrice = row[4]
        #Exclude year(s) 2017
        if rowYear not in EXCLUDE_YEARS and int(rowYear) >= 2010:
            print FILENAME + "," + rowYear + "," + rowMonth + "," + rowDay + "," + closingPrice

    idx = idx + 1