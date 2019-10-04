#!/usr/bin/python
import sys

def process_rating(line):
    avg   = float(line[1])
    num_v = int(line[2])

    if avg >= 7.5 and num_v >= 500000:
        print("%s" % line[0])

def process_basic(line):
    title_type    = line[1]
    primary_title = line[2]
    start_year    = line[5]

    if "\\N" in [title_type, primary_title, start_year]:
        return

    release_year = int(start_year)

    if title_type == "movie" and release_year >= 1990 \
            and release_year <= 2018:

        print("%s\t%s" % (line[0], primary_title))

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        process_rating(line)
    else:
        process_basic(line)
