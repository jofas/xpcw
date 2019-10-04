#!/usr/bin/python
import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    title_type = line[1]
    runtime    = line[-2]
    genres     = line[-1]

    if runtime == "\\N" or genres == "\\N" \
            or title_type != "movie":
        continue

    for genre in genres.split(","):
        print("%s\t%s" % (genre, runtime))
