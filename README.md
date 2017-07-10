# MarketAnalysis

### Run stage1 Map
hadoop jar PATH_TO_HADOOP/hadoop-streaming-2.8.0.jar -mapper /app/stage1/map.py -input "marketdata/DGLT.csv" -output "stage1results"
