#!/usr/bin/env python3

import re

test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

mulre = r'mul\(([0-9]+),([0-9]+)\)'

def run(inp):
    return sum(int(a)*int(b) for a, b in re.findall(mulre, inp))
assert (got := run(test_input)) == 161, got

real_input = open('inputs/day03.input.txt').read()
print(run(real_input)) # => 167090022
