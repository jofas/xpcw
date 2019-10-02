#!/usr/bin/python
import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) > 3:
        title_type = line[1]
        release_year = int(line[5]) if line[5] != "\\N" \
            else 0
        if title_type == "movie" and release_year >= 1990 \
                and release_year <= 2018:
            print("%s\t%s" % (line[0], line[2]))
    else:
        print("%s\t%s\t%s" % tuple(line))
