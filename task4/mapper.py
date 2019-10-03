#!/usr/bin/python
import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 3:
        if line[2] == "\\N":
            continue

        if line[2][:2] == "nm":
            print("%s\t%s\tcrew" % (line[0], line[2]))
        else:
            print("%s\t%s\trating" % (line[0], line[2]))

    else:
        id   = line[0]
        name = line[1]
        prof = line[4]
        titl = line[5]

        if "\\N" in [id, name, prof, titl]:
            continue

        prof = prof.split(",")

        # ! could be necessary to remove
        #if "writer" not in prof:
        #    continue

        titl = titl.split(",")

        for t in titl:
            print("%s\t%s\t%s\tname" % (t, id, name))
