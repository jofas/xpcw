TMP_DIR=/user/$USER/tmp
OUT_DIR=/user/$USER/task3
IN_DIR=/data/small/imdb

hadoop dfs -rm -r $TMP_DIR
hadoop dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.basics.tsv \
  -input $IN_DIR/title.ratings.tsv \
  -output $TMP_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

hadoop -dfs -cat $TMP_DIR/* > $TMP_DIR/job.out

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $TMP_DIR/job.out \
  -output $OUT_DIR \
  -mapper cat \
  -reducer cat \

#-reducer reducer2.py \
#-file reducer2.py
