#!/usr/bin/python
import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    runtime, genres = line[-2], line[-1]

    if runtime == "\\N" or genres == "\\N": continue

    for genre in genres.split(","):
        print("%s|%s" % (genre, runtime))
