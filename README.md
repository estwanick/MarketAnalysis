# MarketAnalysis

##What are we doing?
Calculating and predicting monthly returns for every company in the technology sector with data before 2015

#Run Stage 1
hdfs dfs -rm -r stage1.2sorted

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_sort.py -input "marketdata/" -output "stage1.2sorted" && hdfs dfs -cat stage1.2sorted/part-00000

##Description
Properly format data

#Run Stage 1.1
hdfs dfs -rm -r stage1.2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k2,2n -k3,3n -k4,4n' -mapper app/stage1.2/map_pass.py -reducer app/stage1.2/reduce.py  -input "stage1.2sorted" -output "stage1.2results" && hdfs dfs -cat stage1.2results/part-00000

##Description
Calculate the Monthly Returns for a given stock

#Run Stage 2
hdfs dfs -rm -r stage2results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=6  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage2/map.py  -reducer app/stage2/reduce.py -input "stage1.2results/part-00000" -output "stage2results" && hdfs dfs -cat stage2results/part-00000

##Description
Predict 2015 and 2016 for every month for a stock using every model

#Run Stage 3
hdfs dfs -rm -r stage3results

hadoop jar /Users/michaelestwanick/hadoop-2.8.0/share/hadoop/tools/lib/hadoop-streaming-2.8.0.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=8  -D map.output.key.field.separator=, -D mapred.text.key.comparator.options='-k1,1 -k3,3n -k2,2n' -mapper app/stage3/map.py -reducer app/stage2/reduce.py -input "stage2results/part-00000" -output "stage3results" && hdfs dfs -cat stage3results/part-00000

##Description
Determine the most accurate model for 2015 results and compare that to 2016 results for validation





** Summary of changes
Stage 2 changes ------
use all models to predict 2015

use all models to predict 2016

output 2015 results ... output 2016 results

Stage 3 changes -------
input output 2015 results ... output 2016 results

determine which model was the best for 2015

compare that model to the respective model for 2016 
- ie if LinearRegression won for 2015, compare that to the result of LinearRegression for 2016

using original data we predict 2015 and 2016

1. actual results (2015 models) (2016 models)

2. actual results (2015 choose winner) (2016 results)

3. based on 2015 winner get the value for the corresponding model in 2016

4. Compare the corresponding model of 2016 with the actual returns for 2016








































