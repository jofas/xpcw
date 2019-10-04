#!/usr/bin/python
import sys

cur_movie  = None
cur_crew   = None
cur_rating = None
cur_names  = []

def process_cur():
    if None in [cur_movie, cur_crew, cur_rating]: return

    for name in cur_names:
        if name[0] in cur_crew:
            print("%s\t%s\t%s" % (name[0], cur_rating, name[1]))

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if line[0] == cur_movie:
        if line[-1] == "crew":
            cur_crew = line[1].split(",")
        elif line[-1] == "rating":
            cur_rating = line[1]
        else:
            cur_names.append(line[1:3])
    else:
        process_cur()

        # reset
        cur_movie  = line[0]
        cur_crew   = None
        cur_rating = None
        cur_names  = []

        if line[-1] == "crew":
            cur_crew = line[1].split(",")
        elif line[-1] == "rating":
            cur_rating = line[1]
        else:
            cur_names.append(line[1:3])

process_cur()
