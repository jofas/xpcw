#!/usr/bin/python
import sys

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) > 3:
        t_num        = line[0]
        title_type   = line[1]
        title        = line[2]
        release_year = line[5]
        genres       = line[8]

        if "\\N" in [title_type, genres, release_year]:
            continue

        release_year = int(release_year)

        if title_type == "movie" and release_year >= 1900 \
                and release_year <= 1999:

            decade = (release_year - 1900) / 10

            print("%s\t%s\t%s\t%d" % (t_num, title, genres, decade))
    else:
        print("%s\t%s" % tuple(line[:2]))
