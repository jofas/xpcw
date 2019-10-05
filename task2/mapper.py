#!/usr/bin/python

##Task2
##=====
##
##Titles from movies released between 1990 and 2018
##(inclusive) with an average rating greater equal 7.5 and
##at least 500,000 votes.
##
##
##Output
##------
##
##\[title\]
##
##
##Additional information
##----------------------
##
##* titleType == "movie"
##
##* title := primaryTitle
##
##
##Data sources
##------------
##
##* title.basics.tsv
##
##* title.ratings.tsv
##
##
##Mapper
##======
##
##
##Process basic
##-------------
##
##For each valid line which represents a move released
##in (1990, 2018) return \[tnum, title\].
##
##
##Process rating
##--------------
##
##For each line having an average of at least 7.5 and at
##least 500,000 votes return \[tnum\].
##
##

import sys

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


def process_rating(line):
    avg   = float(line[1])
    num_v = int(line[2])

    if avg >= 7.5 and num_v >= 500000:
        print("%s" % line[0])


for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        process_rating(line)
    else:
        process_basic(line)
