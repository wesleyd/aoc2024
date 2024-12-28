#!/usr/bin/env python3

test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()

def safe0(xx):
    increasing = None
    for a, b in zip(xx, xx[1:]):
        if increasing is None:
            increasing = b > a
        if increasing != (b > a):
            return False
        if abs(b-a) not in [1,2,3]:
            return False
    return True

def safe1(xx):
    if safe0(xx):
        return True
    for i in range(len(xx)):
        if safe0(xx[0:i] + xx[i+1:]):
            return True
    return False

def run(inp):
    nsafe = 0
    for line in inp.splitlines():
        xx = [int(s) for s in line.split()]
        if safe1(xx):
            nsafe += 1
    return nsafe

assert (got := run(test_input)) == 4, got

real_input = open('inputs/day02.input.txt').read().strip()
print(run(real_input)) # => 569
