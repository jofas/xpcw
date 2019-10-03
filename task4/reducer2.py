#!/usr/bin/python
import sys

N = 10
i = 0

already_seen_names = []

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if line[0] in already_seen_names:
        continue

    print("%s|%s" % (line[1], line[2]))

    i += 1

    if i == N: break
