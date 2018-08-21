hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -files mapper.py,reducer.py -input 'inputFile' -output 'outputfile' -mapper mapper.py -reducer reducer.py


