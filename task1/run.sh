hadoop jar /opt/hadoop/hadoop-2.9.2/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
  -input /data/small/imdb/title.basics.tsv \
  -output /user/$USER/$1 \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -file mapper.py \
  -file combiner.py \
  -file reducer.py
