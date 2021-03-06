TMP_DIR=/user/$USER/tmp
OUT_DIR=/user/$USER/assignment/task4
IN_DIR=/data/large/imdb

hdfs dfs -rm -r $TMP_DIR
hdfs dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.crew.tsv \
  -input $IN_DIR/title.ratings.tsv \
  -input $IN_DIR/name.basics.tsv \
  -output $TMP_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D stream.num.map.output.key.fields=3 \
    -D mapreduce.partition.keycomparator.options=-k2,2nr \
    -D mapreduce.job.reduces=1 \
  -input $TMP_DIR/* \
  -output $OUT_DIR \
  -mapper mapper2.py \
  -reducer reducer2.py \
  -file mapper2.py \
  -file reducer2.py

hdfs dfs -cat $OUT_DIR/* | head -20 > output.out

if [ "$1" == "-v" ]; then
  hdfs dfs -cat $OUT_DIR/*
fi
