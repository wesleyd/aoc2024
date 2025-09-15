#!/usr/bin/env python3

def parse(inp):
    return [int(s) for s in inp.split()]

def blink(stones):
    stones2 = []
    for st in stones:
        s = str(st)
        if st == 0:
            stones2.append(1)
        elif (len(s) % 2) == 0:
            midway = len(s)//2
            stones2.append(int(s[:midway]))
            stones2.append(int(s[midway:]))
        else:
            stones2.append(st*2024)
    return stones2

example1 = parse("125 17")
assert (example1 := blink(example1)) == parse("253000 1 7"), example1
assert (example1 := blink(example1)) == parse("253 0 2024 14168"), example1
assert (example1 := blink(example1)) == parse("512072 1 20 24 28676032"), example1
assert (example1 := blink(example1)) == parse("512 72 2024 2 0 2 4 2867 6032"), example1
assert (example1 := blink(example1)) == parse("1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32"), example1
assert (example1 := blink(example1)) == parse("2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"), example1

def run(stones, n=25):
    for i in range(n):
        stones = blink(stones)
        #print(i, stones)
    return len(stones)
assert (got := run(parse("125 17"))) == 55312, got

print(run(parse(open('inputs/day11.input.txt').read())))
