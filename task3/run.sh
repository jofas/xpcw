TMP_DIR=/user/$USER/tmp
OUT_DIR=/user/$USER/assignment/task3
IN_DIR=/data/large/imdb

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
    -D mapreduce.partition.keycomparator.options="-k1,1n -k2,2 -k3,3nr -k4,4" \
    -D mapreduce.partition.keypartitioner.options=-k1,2 \
  -input $TMP_DIR/* \
  -output $OUT_DIR \
  -mapper mapper2.py \
  -reducer reducer2.py \
  -file mapper2.py \
  -file reducer2.py \
  -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hdfs dfs -cat $OUT_DIR/* | head -20 > output.out

if [ "$1" == "-v" ]; then
  hdfs dfs -cat $OUT_DIR/*
fi
