#!/usr/bin/python
import sys

class Accumulator:
    def __init__(self, genre = None, runtime = 0):
        self.genre          = genre
        self.runtime_sum    = runtime
        self.instance_count = 1
        self.max            = runtime
        self.min            = runtime

    def accumulate(self, runtime):
        self.runtime_sum += runtime
        self.instance_count += 1
        if runtime > self.max: self.max = runtime
        if runtime < self.min: self.min = runtime

    def print_line(self):
        print("%s|%d|%d|%d|%d" % (
            self.genre, self.runtime_sum,
            self.instance_count, self.max, self.min ))

line_acc = Accumulator()

for raw_line in sys.stdin:
    line = raw_line.split("|")
    genre, runtime = line[0], int(line[1])

    if genre != line_acc.genre:
        if line_acc.genre != None:
            line_acc.print_line()

        line_acc = Accumulator(genre, runtime)
    else:
        line_acc.accumulate(runtime)

line_acc.print_line()
