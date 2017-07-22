#!/usr/bin/env python
import sys, os, re
from datetime import datetime

PATH = os.environ['mapreduce_map_input_file']
FILENAME = re.search('[^\/]+(\w+)$', PATH).group().replace('.csv', '')

EXCLUDE_YEARS = ['2016', '2017']

idx = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(',')
    rowYear = row[1]
    rowMonth = row[2]
    rowDay = row[3]

    #Skip header row; then start calculating daily returns at second row
    if idx == 0:
        previousClosingPrice = float(row[4])

    if idx > 0:
        closingPrice = float(row[4])
        dailyReturnPercent = (closingPrice / previousClosingPrice) - 1
        previousClosingPrice = closingPrice
    
        #Exclude years 2016,2017
        if rowYear in EXCLUDE_YEARS:
            print row[0] + "," + rowYear + "," + rowMonth + "," + rowDay + "," + str(dailyReturnPercent)

    idx = idx + 1
