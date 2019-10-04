#!/usr/bin/python
import sys

cur_basic  = None
cur_rating = None

def process_cur():
    if cur_basic != None and cur_rating != None:
        if cur_basic[0] == cur_rating[0]:
            print("%s" % cur_basic[1])

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 1:
        cur_rating = line
    elif len(line) == 2:
        cur_basic = line
    else:
        print("%s" % line[0])
        continue

    process_cur()

process_cur()
