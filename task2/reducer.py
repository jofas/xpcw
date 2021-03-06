#!/usr/bin/python

##Reducer
##=======
##
##Prints each move title which has two lines. Only movies
##which fulfill the defined criterias are represented by
##two lines, since the movie from title.ratings.tsv is
##otherwise omitted.
##
##

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
    else:
        cur_basic = line

    process_cur()

process_cur()
