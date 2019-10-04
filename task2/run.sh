OUT_DIR=/user/$USER/assignment/task2
IN_DIR=/data/small/imdb

hadoop dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.basics.tsv \
  -input $IN_DIR/title.ratings.tsv \
  -output $OUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

hdfs dfs -cat $OUT_DIR/* | head -20 > output.out

if [ "$1" == "-v" ]; then
  hdfs dfs -cat $OUT_DIR/*
fi
