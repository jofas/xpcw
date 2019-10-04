#!/usr/bin/python
import sys

from bisect import insort

N = 10

BIGGEST = []

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    votes = int(line[1])

    inserted = False
    for i in range(len(BIGGEST)):
        if votes >= BIGGEST[i][1]:
            BIGGEST.insert(line, i)
            inserted = True
            break

    if len(BIGGEST) < N and not inserted:
        BIGGEST.append(line)

    if len(BIGGEST) > N:
        BIGGEST = BIGGEST[:N]

for line in BIGGEST:
    print("%s\t%s\t%s" % tuple(line))
