#!/usr/bin/env python3

from functools import reduce

import operator
import re

def calc(inp):
    ret = 0
    for m in re.findall(r"mul\((\d+),(\d+)\)", inp):
        ret += int(m[0]) * int(m[1])
    return ret
assert(calc("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")) == 161

print(calc(open('inputs/day03.input.txt').read()))

###

def calc2(inp):
    ret = 0
    do = True
    for m in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", inp):
        if m == r"do()":
            do = True
        elif m == r"don't()":
            do = False
        elif do:
            ret += reduce(operator.mul, map(int, re.findall("\d+", m)))
    return ret
assert ((x := calc2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")) == 48), x

print(calc2(open('inputs/day03.input.txt').read()))
