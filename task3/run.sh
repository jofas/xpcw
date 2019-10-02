OUT_DIR=/user/$USER/task3
IN_DIR=/data/small/imdb

hadoop dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.basics.tsv \
  -input $IN_DIR/title.ratings.tsv \
  -output $OUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -mapper sort \
  -file mapper.py \
  -file reducer.py
