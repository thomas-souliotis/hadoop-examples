hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.job.reduces=1 -input 'inputFile' -output 'outputFile' -mapper mapper.py -combiner reducer.py -reducer reducer.py -file mapper.py -file reducer.py

