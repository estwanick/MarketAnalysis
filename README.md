# MarketAnalysis

#### Stage 1
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' -mapper app/stage1/map.py  -reducer app/stage1/reduce.py -input "marketdata/AAPL.csv" -output "stage1results" && hdfs dfs -cat stage1results/part-00000

#### Stage 1.1
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' -mapper app/stage1.1/map.py  -reducer app/stage1.1/reduce.py -input "marketdata/AAPL.csv" -output "stage1.1results" && hdfs dfs -cat stage1results/part-00000

#### Stage 1.2
###### Use daily returns instead of monthly volatility

hdfs dfs -rm -r stage1.2sorted

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_sort.py -input "marketdata/DGLT.csv" -output "stage1.2sorted" && hdfs dfs -cat stage1.2sorted/part-00000


hdfs dfs -rm -r stage1.2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map.py  -input "stage1.2sorted" -output "stage1.2results" && hdfs dfs -cat stage1.2results/part-00000




#Run Stage2
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -input "stage1results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000


#Just mapper
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -input "stage1results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

#stage2 with mapper and reducer
hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -reducer app/stage2/reduce.py -input "stage1results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

#delet s2 results
hdfs dfs -rm -r stage2results















































