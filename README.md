# MarketAnalysis

#### To RUN
###### Use daily returns instead of monthly volatility

hdfs dfs -rm -r stage1.2sorted

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_sort.py -input "marketdata/" -output "stage1.2sorted" && hdfs dfs -cat stage1.2sorted/part-00000


hdfs dfs -rm -r stage1.2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_pass.py -reducer app/stage1.2/reduce.py  -input "stage1.2sorted" -output "stage1.2results" && hdfs dfs -cat stage1.2results/part-00000

hdfs dfs -rm -r stage2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -reducer app/stage2/reduce.py -input "stage1.2results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

hdfs dfs -rm -r stage3results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=8  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage3/map.py -input "stage2results/part-00000" -output "stage3results" && hdfs dfs -cat stage3results/part-00000












































