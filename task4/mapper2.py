#!/usr/bin/python

##Mapper 2
##========
##
##In-mapper combiner for reducing network traffic.
##
##Every mapper has a list of 10 elements which contain the
##most popular writers the mapper instance encounters.
##
##For every line of the 10 most popular writers return
##\[nconst, rating, name\].
##
##

import sys

N = 10

BIGGEST = []

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    votes = int(line[1])

    inserted = False
    for i in range(len(BIGGEST)):
        if votes >= int(BIGGEST[i][1]):
            BIGGEST.insert(i, line)
            inserted = True
            break

    if len(BIGGEST) < N and not inserted:
        BIGGEST.append(line)

    if len(BIGGEST) > N:
        BIGGEST.pop()

for line in BIGGEST:
    print("%s\t%s\t%s" % tuple(line))
