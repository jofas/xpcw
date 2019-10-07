#!/usr/bin/python

##Task 1
##======
##
##Retrieve average, minimum and maximum duration for all
##titles per *movie* genre.
##
##
##Output
##------
##
##\[avg|max|min|genre\]
##
##
##Additional information
##----------------------
##
##* title -> genre: 1 -> n (title should be considered for
##                          all associated genres)
##
##* avg: in minutes and rounded to two decimal places
##
##* runtime = 0 should be considered in computation
##
##
##Data sources
##------------
##
##* title.basics.tsv
##
##
##Mapper
##======
##
##For each valid line return \[genre, runtime\].
##
##

import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    title_type = line[1]
    runtime    = line[-2]
    genres     = line[-1]

    if runtime == "\\N" or genres == "\\N":
        continue

    for genre in genres.split(","):
        print("%s\t%s" % (genre, runtime))
