#!/usr/bin/env python3

from functools import cache

def parse(inp):
    return [int(s) for s in inp.split()]

@cache
def blink1(stone, n):
    if n == 0:
        return 1
    s = str(stone)
    if stone == 0:
        return blink1(1, n-1)
    elif (len(s) % 2) == 0:
        midway = len(s)//2
        return blink1(int(s[midway:]), n-1) + blink1(int(s[:midway]), n-1)
    else:
        return blink1(stone*2024, n-1)

def blink(stones, n):
    return sum([blink1(stone, n) for stone in stones])

assert (got := blink(parse("125 17"), 25)) == 55312, got

print(blink(parse(open('inputs/day11.input.txt').read()), 75))
