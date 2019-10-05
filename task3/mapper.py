#!/usr/bin/python
import sys

##Task3
##=====
##
##Print the top rated movie for each genre for each decade
##of the 20th century.
##
##
##Output
##------
##
##\[decade|genre|title\]
##
##
##Additional information
##----------------------
##
##* titleType == "movie"
##
##* output sorted by decade, genre
##
##* if two or more top rated movies: 1st in alphabetical
##  order
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
##For each valid line which represents a movie from the
##20th century return \[tnum, title, genres, decade\].
##
##
##Process rating
##--------------
##
##For each line return \[tnum, avg\].
##
##

def process_basic(line):
    t_num        = line[0]
    title_type   = line[1]
    title        = line[2]
    release_year = line[5]
    genres       = line[8]

    if "\\N" in [title_type, title, genres, release_year]:
        return

    release_year = int(release_year)

    if title_type == "movie" and release_year >= 1900 \
            and release_year <= 1999:

        decade = (release_year - 1900) / 10

        print("%s\t%s\t%s\t%d" % (t_num, title, genres, decade))

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        print("%s\t%s" % tuple(line[:2]))
    else:
        process_basic(line)
