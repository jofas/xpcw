#!/usr/bin/python
import sys

from util import MovieProcessor

proc = MovieProcessor()

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 1:
        print("%s" % line[0])
    else:
        proc.process(line)
