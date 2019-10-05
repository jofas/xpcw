#!/usr/bin/python

##Mapper 2
##========
##
##In-mapper combiner for reducing network traffic.
##
##For each decade and genre, the title with the best rating
##is saved and the others are disregarded.
##
##Returns \[decade, genre, avg, title\].
##
##

import sys

MAP = {}
MAX_LEN = 100

def print_map():
    for d in MAP:
        for g in MAP[d]:
            print("%s\t%s\t%.1f\t%s" % (
                d, g, MAP[d][g][0], MAP[d][g][1]
            ))

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    decade = line[0]
    genre  = line[1]
    rating = float(line[2])
    title  = line[3]

    if MAP.has_key(decade):
        if MAP[decade].has_key(genre):
            entry = MAP[decade][genre]
            if rating > entry[0] or (rating == entry[0]
                    and title < entry[1]):
                MAP[decade][genre] = [rating, title]
        else:
            MAP[decade][genre] = [rating, title]
    else:
        MAP[decade] = {}
        MAP[decade][genre] = [rating, title]

    if len(MAP) == 100:
        print_map()

print_map()
