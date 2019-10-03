TMP_DIR=/user/$USER/tmp
OUT_DIR=/user/$USER/task4
IN_DIR=/data/small/imdb

hdfs dfs -rm -r $TMP_DIR
hdfs dfs -rm -r $OUT_DIR

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input $IN_DIR/title.basics.tsv \
  -input $IN_DIR/title.ratings.tsv \
  -output $TMP_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py

hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D stream.num.map.output.key.fields=4 \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2nr" \
    -D mapreduce.partition.keypartitioner.options=-k1 \
  -input $TMP_DIR/* \
  -output $OUT_DIR \
  -mapper cat \
  -reducer cat \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat $OUT_DIR/*

