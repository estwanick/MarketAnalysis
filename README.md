# MarketAnalysis

## What are we doing?
Calculating and predicting monthly returns for every company in the technology sector with data before 2015

# Stage1
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=3  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' -mapper app/stage1/map.py -reducer app/stage1/reduce.py -input "marketdata/AABA.csv" -output "stage1results" && hdfs dfs -cat stage1results/part-00000

# Stage2
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=3  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py -reducer app/stage2/reduce.py -input "stage1results" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

# Stage3
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=3  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage3/map.py -reducer app/stage3/reduce.py -input "stage2results" -output "stage3results" && hdfs dfs -cat stage3results/part-00000







































