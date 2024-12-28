#!/usr/bin/env python3

from collections import defaultdict

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

def hashcount(xx):
    counts = defaultdict(int)
    for x in xx:
        counts[x]+=1
    return counts

def run(inp):
    aa, bb = vsplit(inp)
    bc = hashcount(bb)
    similarity = 0
    for a in aa:
        similarity += a * bc[a]
    return similarity

assert (got := run(test_input)) == 31, got

real_input = open('inputs/day01.input.txt').read().strip()
print(run(real_input))  # => 18567089
