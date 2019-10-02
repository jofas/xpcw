#!/usr/bin/python
import sys

from util import MovieProcessor

proc = MovieProcessor()

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")
    proc.process(line)

