#!/usr/bin/python
import sys

def process_crew_or_ratings(line):
    if line[2] == "\\N":
        return

    if line[2][:2] == "nm":
        print("%s\t%s\tcrew" % (line[0], line[2]))
    else:
        print("%s\t%s\trating" % (line[0], line[2]))

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

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        process_crew_or_ratings(line)
    else:
        process_names(line)
