# Project Description

Use Hadoop MadReduce to predict the Monthly Stock Volatility of a set a stocks
- We tested on top 50 technology stocks and top 100 technology stocks

- Link to presentation: https://docs.google.com/presentation/d/1oP_uZN4aAAPVfrW7btLF0oZ7IY1ljW8ZjDTEopfHIDA/edit?usp=sharing

### S3 Data Resources
- https://s3.amazonaws.com/monthly-volatility-data/tech50/
- https://s3.amazonaws.com/monthly-volatility-data/tech100/

### Amazon EMR Settings
- S3 Bucket Name: https://s3.console.aws.amazon.com/s3/buckets/monthly-volatility-mapreduce/
- File Structure on S3
    - /monthly-volatility-mapreduce
        - /stage1
            - map.py
            - reduce.py
        - /stage2
            - map.py
            - reduce.py
        - /stage3
            - map.py
            - reduce.py

- Quick Links
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage1/map.py
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage1/reduce.py
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage2/map.py
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage2/reduce.py
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage3/map.py
    - https://s3.amazonaws.com/monthly-volatility-mapreduce/stage3/reduce.py

- Boostrap script location: s3://monthly-volatility-mapreduce/boostrap.sh
- Boostrap script settings can be found under *Advanced Options when creating your EMR Cluster

### Stage 1

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D map.output.key.field.separator=, -D mapred.text.key.comparator.options=-k1,1 -files s3://monthly-volatility-mapreduce/stage1/map.py,s3://monthly-volatility-mapreduce/stage1/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-data/tech50 -output s3://monthly-volatility-output/stage1results

### Stage 2

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=1 -D map.output.key.field.separator=, -files s3://monthly-volatility-mapreduce/stage2/map.py,s3://monthly-volatility-mapreduce/stage2/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-output/stage1results -output s3://monthly-volatility-output/stage2results

### Stage 3

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=1 -D map.output.key.field.separator=, -files s3://monthly-volatility-mapreduce/stage3/map.py,s3://monthly-volatility-mapreduce/stage3/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-output/stage2results -output s3://monthly-volatility-output/stage3results






































