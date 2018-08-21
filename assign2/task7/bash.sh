pv 'inputFile' | parallel --pipe ./mapper.py  |./reducer.py  > 'outputFile' 
