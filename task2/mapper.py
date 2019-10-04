#!/usr/bin/python
import sys

MAX_SIZE = 100
VALS = {}

def process_rating(line):
    avg   = float(line[1])
    num_v = int(line[2])

    if avg >= 7.5 and num_v >= 500000:
        if VALS.has_key(line[0]):
            print("%s\t\\N\t\\N" % VALS[line[0]])
            del VALS[line[0]]
        else:
            VALS[line[0]] = None

def process_basic(line):
    title_type    = line[1]
    primary_title = line[2]
    start_year    = line[5]

    if "\\N" in [title_type, primary_title, start_year]:
        return

    release_year = int(start_year)

    if title_type == "movie" and release_year >= 1990 \
            and release_year <= 2018:

        if VALS.has_key(line[0]):
            print("%s\t\\N\t\\N" % primary_title)
            del VALS[line[0]]
        else:
            VALS[line[0]] = primary_title

def clear_vals():
    for k, v in VALS.items():
        if v == None:
            print("%s" % k)
        else:
            print("%s\t%s" % (k, v))
    VALS.clear()

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        process_rating(line)
    else:
        process_basic(line)

    if len(VALS) == MAX_SIZE:
        clear_vals()

clear_vals()
