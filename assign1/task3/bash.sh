hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.job.reduces=1 -files mapper.py,reducer.py -input 'inputFile' -output 'outputFile' -mapper mapper.py -reducer reducer.py


