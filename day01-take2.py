#!/usr/bin/env python3

from collections import defaultdict

def parse(f):
    aa, bb = [], []
    for l in f.readlines():
        ss = l.split()
        aa.append(int(ss[0]))
        bb.append(int(ss[1]))
    return aa, bb


with open('inputs/day01.input.txt') as f:
    left, right = parse(f)
    left.sort()
    right.sort()

tot = 0
for l, r in zip(left, right):
    tot += abs(l-r)
print(tot)

###

tot2 = 0
rm = defaultdict(int)
for r in right:
    rm[r] += 1
for l in left:
    tot2 += l * rm[l]
print(tot2)
