#!/usr/bin/python
import sys

class MovieProcessor:
    def __init__(self, len_basic, len_rating, processor):
        self.basic  = []
        self.rating = []

        self.len_basic  = len_basic
        self.len_rating = len_rating

        self.processor = processor

    def process(self, line):
        if len(line) == self.len_basic and \
                len(self.rating) == self.len_rating:

            if line[0] == self.rating[0]:
                self.processor(line, self.rating)
                self.basic = []
            else:
                self.basic = line
            self.rating = []

        elif len(line) == self.len_rating and \
                len(self.basic) == self.len_basic:

            if line[0] == self.basic[0]:
                self.processor(self.basic, line)
                self.rating = []
            else:
                self.rating = line
            self.basic = []

        elif len(line) == self.len_basic and \
                len(self.rating) == 0:

            self.basic = line

        elif len(line) == self.len_rating and \
                len(self.basic) == 0:

            self.rating = line

def processor(basic, rating):
    if float(rating[1]) >= 7.5 \
            and int(rating[2]) >= 500000:
        print("%s" % basic[1])

proc = MovieProcessor(2, 3, processor)

for raw_line in sys.stdin:
    line = raw_line.strip().split("\t")
    proc.process(line)
