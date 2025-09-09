#!/usr/bin/env python3

def safe(levels):
    if type(levels) == str:
        levels = [int(n) for n in levels.split()]
    sign = +1 if levels[0] < levels[1] else -1
    for i in range(0, len(levels)-1):
        delta = abs(levels[i] - levels[i+1])
        if delta < 1 or 3 < delta:
            return False
        s = +1 if levels[i] < levels[i+1] else -1
        if s != sign:
            return False
    return True

assert safe("7 6 4 2 1")
assert not safe("1 2 7 8 9")
assert not safe("9 7 6 2 1")
assert not safe("1 3 2 4 5")
assert not safe("8 6 4 4 1")
assert safe("1 3 6 7 9")

nsafe = 0
for report in open('inputs/day02.input.txt').readlines():
    if safe(report):
        nsafe += 1
print(nsafe)

###

def safe2(levels):
    levels = [int(n) for n in levels.split()]
    if safe(levels):
        return True
    for i in range(len(levels)):
        if safe(levels[:i] + levels[i+1:]):
            return True
    return False

assert safe2("7 6 4 2 1")
assert not safe2("1 2 7 8 9")
assert not safe2("9 7 6 2 1")
assert safe2("1 3 2 4 5")
assert safe2("8 6 4 4 1")
assert safe2("1 3 6 7 9")

nsafe = 0
for report in open('inputs/day02.input.txt').readlines():
    if safe2(report):
        nsafe += 1
print(nsafe)
