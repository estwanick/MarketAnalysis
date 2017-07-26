# MarketAnalysis

<<<<<<< HEAD
#### To RUN
###### Use daily returns instead of monthly volatility

hdfs dfs -rm -r stage1.2sorted

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_sort.py -input "marketdata/" -output "stage1.2sorted" && hdfs dfs -cat stage1.2sorted/part-00000


hdfs dfs -rm -r stage1.2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_pass.py -reducer app/stage1.2/reduce.py  -input "stage1.2sorted" -output "stage1.2results" && hdfs dfs -cat stage1.2results/part-00000

hdfs dfs -rm -r stage2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -reducer app/stage2/reduce.py -input "stage1.2results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

hdfs dfs -rm -r stage3results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=8  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage3/map.py -reducer app/stage2/reduce.py -input "stage2results/part-00000" -output "stage3results" && hdfs dfs -cat stage3results/part-00000







































=======
#### Sample Command to run MapReduce Job
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar 
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator 
-D stream.map.output.field.separator=, 
-D stream.num.map.output.key.fields=5  
-D map.output.key.field.separator=, 
-D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' 
-mapper app/stage1/map.py 
-reducer app/stage1/reduce.py 
-input "marketdata/FB.csv" 
-output "stage1results" 
&& hdfs dfs -cat stage1results/part-00000

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


matt command:
hadoop jar ../../usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=4 -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper marketanalysis/app/stage2/map.py  -input "stage1results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000 


matt stage1 command:
hadoop jar ../../usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6 -D map.output.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' -mapper marketanalysis/app/stage1/map.py -reducer marketanalysis/app/stage1/reduce.py -input "AAPL" -output "stage1results" && hdfs dfs -cat stage1results/part-00000 
>>>>>>> ff566dea60ee08984f8a2d0fca53636c811d8ed5





