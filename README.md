# MarketAnalysis

/Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -mapper /home/ubuntu/map.py -reducer /home/ubuntu/reduce.py -input "states" -output "stage1results"

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -mapper /app/stage1/map.py -input "marketdata/DGLT.csv" -output "stage1results"

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=3  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2 -k3,3nr' -mapper app/stage1/map.py -input "marketdata/DGLT.csv" -output "stage1results" && hdfs dfs -cat stage1results/part-00000

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=5  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n' -mapper app/stage1/map.py -reducer app/stage1/reduce.py -input "marketdata/FB.csv" -output "stage1results" && hdfs dfs -cat stage1results/part-00000