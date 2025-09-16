#!/usr/bin/env python3

from dataclasses import dataclass
import re

example_input = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

@dataclass
class Machine:
    ax: int = 0
    ay: int = 0
    bx: int = 0
    by: int = 0
    px: int = 0
    py: int = 0

def parse(inp):
    machines = []
    for para in inp.split("\n\n"):
        nn = map(int, re.findall(r"\d+", para))
        machines.append(Machine(*nn))
    return machines

def solutions(m: Machine):
    min_cost = 0
    for a in range(101):
        x = m.ax*a
        y = m.ay*a
        if x > m.px or y > m.py:
            break
        if (m.px - x) % m.bx == 0 and (m.py - y) % m.by == 0 and (b := (m.px - x) // m.bx) == (m.py - y) // m.by:
            cost = 3*a + b
            if not min_cost or cost < min_cost:
                min_cost = cost
    return min_cost

def play(machines):
    return sum(map(solutions, machines))

assert (got := play(parse(example_input))) == 480, got

print(play(parse(open('inputs/day13.input.txt').read())))
