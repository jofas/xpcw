#!/usr/bin/python
import sys

cur_basic = None
cur_rating = None

def process_cur():
    if cur_basic != None and cur_rating != None:
        if cur_basic[0] == cur_rating[0]:
            genres = cur_basic[2].split(",")

            for genre in genres:
                print("%s\t%s\t%s\t%s" % (
                    cur_basic[3], genre, cur_rating[1], cur_basic[1]
                ))

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 2:
        cur_rating = line
    else:
        cur_basic = line

    process_cur()

process_cur()
