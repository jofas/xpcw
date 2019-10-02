#!/usr/bin/python
import sys

cur_decade = None
cur_genre = None

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    decade = int(line[0])
    genre  = line[1]

    if decade != cur_decade:
        cur_decade = decade
        cur_genre  = None

    if genre != cur_genre:
        print ("%s|%s|%s" % (decade, genre, line[3]))
        cur_genre = genre
