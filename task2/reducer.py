#!/usr/bin/python
import sys

class MovieProcessor:
    def __init__(self):
        self.basic  = []
        self.rating = []

    def process(self, line):
        if len(line) == 2 and len(self.rating) == 3:
            if line[0] == self.rating[0]:
                self.process_movie(line, self.rating)
                self.basic = []
            else:
                self.basic = line
            self.rating = []

        elif len(line) == 3 and len(self.basic) == 2:
            if line[0] == self.basic[0]:
                self.process_movie(self.basic, line)
                self.rating = []
            else:
                self.rating = line
            self.basic = []

        elif len(line) == 2 and len(self.rating) == 0:
            self.basic = line

        elif len(line) == 3 and len(self.basic) == 0:
            self.rating = line

    def process_movie(self, basic, rating):
        if float(rating[1]) >= 7.5 \
                and int(rating[2]) >= 500000:
            print("%s" % basic[1])

proc = MovieProcessor()

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")

    if len(line) == 1:
        print("%s" % line[0])
    else:
        proc.process(line)
