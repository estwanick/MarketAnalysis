#!/usr/bin/env python
import sys, os, re
from datetime import datetime

PATH = os.environ['mapreduce_map_input_file']
FILENAME = re.search('[^\/]+(\w+)$', PATH).group().replace('.csv', '')
MONTHS = ["Unknown",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

idx = 0
for line in sys.stdin:
    line = line.strip()
    row = line.split(',')
    #Skip header row
    if idx != 0:
        rowDate = datetime.strptime(str(row[0]), '%Y-%m-%d')
        rowYear = str(rowDate.year)
        rowMonth = MONTHS[rowDate.month]
        closingPrice = row[4]
        print FILENAME + "," + rowYear + "," + rowMonth + "," + closingPrice
    idx = idx + 1
