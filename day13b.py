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
        m = Machine(*map(int, re.findall(r"\d+", para)))
        m.px += 10000000000000
        m.py += 10000000000000
        machines.append(m)
    return machines

def solve(m):
    det = abs(m.ax * m.by - m.ay * m.bx)
    if det == 0:
        return 0
    a = int((m.by*m.px - m.bx*m.py)/det)
    b = int((-m.ay*m.px + m.ax*m.py)/det)
    if a < 0 and b < 0:
        a, b = -a, -b
    if a < 0 or b < 0:
        return 0
    if a*m.ax + b*m.bx != m.px or a*m.ay + b*m.by != m.py:
        return 0
    return 3*a + b

def play(machines):
    return sum(solve(m) for m in machines)

print(play(parse(open('inputs/day13.input.txt').read())))
