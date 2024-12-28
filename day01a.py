#!/usr/bin/env python3

import operator

test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()

def vsplit(inp):
    aa, bb = [], []
    for line in inp.splitlines():
        a, b = map(int, line.split())
        aa.append(a)
        bb.append(b)
    return aa, bb

def ordered_deltas(aa, bb):
    for a, b in zip(sorted(aa), sorted(bb)):
        yield abs(a-b)

def run(inp):
    return sum(ordered_deltas(*vsplit(inp)))

assert (got := run(test_input)) == 11, got

real_input = open('inputs/day01.input.txt').read().strip()
print(run(real_input))  # => 2000468
