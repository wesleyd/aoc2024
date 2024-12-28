#!/usr/bin/env python3

import re

test_input = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

allre = r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)'
mulre = r'mul\(([0-9]+),([0-9]+)\)'

def run(inp):
    sum = 0
    multiply = True
    for m in re.findall(allre, inp):
        if m == 'do()':
            multiply = True
        elif m == "don't()":
            multiply = False
        if multiply and (m2 := re.match(mulre, m)):
            sum += int(m2.group(1)) * int(m2.group(2))
    return sum
assert (got := run(test_input)) == 48, got

real_input = open('inputs/day03.input.txt').read()
print(run(real_input)) # => 89823704
