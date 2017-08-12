# Project Description

Use Hadoop MadReduce to predict the Monthly Stock Volatility of a set a stocks
- We tested on top 50 technology stocks and top 100 technology stocks

- Link to presentation: https://docs.google.com/presentation/d/1oP_uZN4aAAPVfrW7btLF0oZ7IY1ljW8ZjDTEopfHIDA/edit?usp=sharing

### Instructions for running
- Setup EMR Cluster
- In the advanced options settings for EMR select boostrap script
	- Under additional Options select Boostrap Actions
		- For add bootstrap action select (custom action)
		- Add this to the script location: s3://monthly-volatility-mapreduce/boostrap.sh
		- This will install Scipy, Numpy and Scikit Learn to all nodes in the cluster

- After the cluster is setup
	- Under *Steps set the following settings
		- Step type: Customer JAR
		- Name: Stage(n) MapReduce
		- JAR Location: command-runner.jar
		- Arguments: (Copy and paste one of the scripts below), the order for running the scripts is (Stage 1, Stage 2, Stage 3)
		- Action on Failure: Continue


#### Stage 1

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D map.output.key.field.separator=, -files s3://monthly-volatility-mapreduce/stage1/map.py,s3://monthly-volatility-mapreduce/stage1/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-data/tech50 -output s3://monthly-volatility-output/stage1results

#### Stage 2

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=1 -D map.output.key.field.separator=, -files s3://monthly-volatility-mapreduce/stage2/map.py,s3://monthly-volatility-mapreduce/stage2/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-output/stage1results -output s3://monthly-volatility-output/stage2results

#### Stage 3

hadoop-streaming -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D stream.map.output.field.separator=, -D stream.num.map.output.key.fields=1 -D map.output.key.field.separator=, -files s3://monthly-volatility-mapreduce/stage3/map.py,s3://monthly-volatility-mapreduce/stage3/reduce.py -mapper map.py -reducer reduce.py -input s3://monthly-volatility-output/stage2results -output s3://monthly-volatility-output/stage3results


### Results

#### Cluster with 1 Master node and 4 Slave Nodes on Top 50 technology companies
    - Stage 1 
        - Execution time 1 minute
    - Stage 2
        - Execution time 1 minute
    - Stage 3
        - Execution time 1 minute

#### Cluster with 1 Master node and 8 Slave Nodes on Top 50 technology companies
    - Stage 1 
        - Execution time 1 minutes
    - Stage 2
        - Execution time 1 minutes
    - Stage 3
        - Execution time 1 minutes


#### Cluster with 1 Master node and 4 Slave Nodes on Top 100 technology companies
    - Stage 1 
        - Execution time 2 minutes
    - Stage 2
        - Execution time 1 minute
    - Stage 3
        - Execution time 1 minute

#### Cluster with 1 Master node and 8 Slave Nodes on Top 100 technology companies
    - Stage 1 
        - Execution time 1 minute
    - Stage 2
        - Execution time 1 minute 
    - Stage 3
        - Execution time less than 1 minute


#### Cluster with 1 Master node and 4 Slave Nodes on Top 400+ technology companies
    - Stage 1 
        - Execution time 7 minutes
    - Stage 2
        - Execution time 1 minute
    - Stage 3
        - Execution time 1 minute 

#### Cluster with 1 Master node and 8 Slave Nodes on Top 400+ technology companies
    - Stage 1 
        - Execution time 4 minutes
    - Stage 2
        - Execution time  1 minute
    - Stage 3
        - Execution time 48 seconds

----------------------------------------------------------------------------------

### Fault Tolerance 

#### Description of test 1
- Cluster with 1 Master node and 4 Slave Nodes on Top 400+ technology companies
- Run Stage 1
- 2 nodes fail
- EMR replaces with 2 new nodes

#### Results
- Execution time 19 minutes

#### Description of test 2
- Cluster with 1 Master node and 4 Slave Nodes on Top 400+ technology companies
- Run Stage 1
- All data nodes fail (4 nodes)

#### Results
- (Job failed)All slaves in the job flow were terminated 

#### Description of test 3
- Cluster with 1 Master node and 4 Slave Nodes on Top 400+ technology companies
- Run Stage 1
- Name node fails

#### Results
- (Job failed) The master node was terminated and cannot recover 

----------------------------------------------------------------------------------

### Other information (S3 Buckets are no longer public)

#### S3 Data Resources
- https://s3.amazonaws.com/monthly-volatility-data/tech50/
- https://s3.amazonaws.com/monthly-volatility-data/tech100/
- https://s3.amazonaws.com/monthly-volatility-data/tech400/

#### Amazon EMR Settings
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




































