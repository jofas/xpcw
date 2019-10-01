#!/usr/bin/python
import sys

class Accumulator:
    def __init__(self, line = [None, 0, 0, 0, 0]):
        self.genre          = line[0]
        self.runtime_sum    = int(line[1])
        self.instance_count = int(line[2])
        self.max            = int(line[3])
        self.min            = int(line[4])

    def accumulate(self, line):
        self.runtime_sum += int(line[1])
        self.instance_count += int(line[2])

        max = int(line[3])
        min = int(line[4])

        if max > self.max: self.max = max
        if min < self.min: self.min = min

    def print_line(self):
        print("%.2f|%d|%d|%s" % (
            float(self.runtime_sum) / float(self.instance_count),
            self.max, self.min, self.genre ))


line_acc = Accumulator()

for raw_line in sys.stdin:
    line = raw_line.split("\t")

    if line[0] != line_acc.genre:
        if line_acc.genre != None:
            line_acc.print_line()

        line_acc = Accumulator(line)
    else:
        line_acc.accumulate(line)

line_acc.print_line()
