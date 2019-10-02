OUT_DIR=/user/$USER/task2
IN_DIR=/data/small/imdb

hadoop dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.basics.tsv \
  -output $OUT_DIR \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -file mapper.py \
  -file combiner.py \
  -file reducer.py