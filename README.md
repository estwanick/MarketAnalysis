# MarketAnalysis

#Run Stage1 MR
hadoop jar PATH TO HADOOP/hadoop-streaming-2.8.0.jar -mapper /home/ubuntu/map.py -reducer /home/ubuntu/reduce.py -input "states" -output "stage1results"

#Run Stage1 Map
hadoop jar PATH TO HADOOP/hadoop-streaming-2.8.0.jar -mapper /app/stage1/map.py -input "marketdata/DGLT.csv" -output "stage1results"
