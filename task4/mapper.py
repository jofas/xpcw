#!/usr/bin/python

##Task4
##=====
##
##Print the top 10 most popular writers (based on the
##amount of votes for their most voted title).
##
##
##Output
##------
##
##\[votes|writer\]
##
##
##Additional information
##----------------------
##
##* writer must be in crew for the movie
##
##* output in descending order (no dublicate writers)
##
##
##Data sources
##------------
##
##* title.rating.tsv
##
##* title.crew.tsv
##
##* name.basics.tsv
##
##
##Mapper
##======
##
##
##Process names
##-------------
##
##For every valid line, check if person is a writer and
##for each title the writer is associated with return
##\[tnum, nconst, name, "name"\].
##
##
##Process rating and crew
##-----------------------
##
##For every valid line return \[tnum, num_votes/writers,
##"rating"/"crew"\].
##
##

import sys

def process_names(line):
    id   = line[0]
    name = line[1]
    prof = line[4]
    titl = line[5]

    if "\\N" in [name, prof, titl]:
        return

    prof = prof.split(",")

    # ! could be necessary to remove
    if "writer" not in prof:
        return

    titl = titl.split(",")

    for t in titl:
        print("%s\t%s\t%s\tname" % (t, id, name))


def process_crew_or_ratings(line):
    if line[2] == "\\N":
        return

    if line[2][:2] == "nm":
        print("%s\t%s\tcrew" % (line[0], line[2]))
    else:
        print("%s\t%s\trating" % (line[0], line[2]))


for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        process_crew_or_ratings(line)
    else:
        process_names(line)
