#!/usr/bin/env python

import sys

ticker = None
closingPrice = None
month = None
year = None
sumClosingPrice = 0;

for line in sys.stdin:
    line = line.strip()
    lineParams = line.split(',')

    cTicker = lineParams[0]
    cYear = lineParams[1]
    cMonth = lineParams[2]
    cOpeningPrice = float(lineParams[3])
    cClosingPrice = float(lineParams[4])

    if (ticker == cTicker) and (month == cMonth) and (year == cYear):
        sumClosingPrice += cClosingPrice
    else:
        if ticker:
            print '%s,%s,%s,%s' % (ticker, year, month, sumClosingPrice)
        ticker = cTicker
        year = cYear
        month = cMonth

# do not forget to output the last word if needed!
# if (current_word == word) and (current_state == state):
#     print '%s\t%s\t%s' % (current_state, current_word, current_count)