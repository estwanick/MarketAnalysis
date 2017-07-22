# MarketAnalysis

#### Sample Command to run MapReduce Job
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1/map.py  -reducer app/stage1/reduce.py -input "marketdata/AAPL.csv" -output "stage1results" && hdfs dfs -cat stage1results/part-00000

#include this at the top of python files
#!/usr/bin/env python

#### Notes from latest discussion MapReduce Stage2
FB,2017,7,1.205329311
# output
ticker, year, month, (stdev per month)

# sort by 
ticker, month, year, (stdev per month)

# sample key order
stream.num.map.output.key.fields=5  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,3n -k3,2n'
# run map and do nothing, then sort by '-k1,1 -k2,3n -k3,2n'
- FB 1 2010 7.14022
- FB 1 2011 7.10422
- FB 1 2012 7.305422
- FB 1 2013 7.103422
- FB 1 2014 predict this 

# what is acceptable range? +-.5

#Run Stage2
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py -input "stage1results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000