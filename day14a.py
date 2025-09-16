#!/usr/bin/env python3

from dataclasses import dataclass
from operator import mul
import re

example_input ="""\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

def parse(inp):
    return [Robot(*map(int, re.findall(r'-?\d+', line))) for line in inp.splitlines()]

class Grid:
    def __init__(self, width, height, inp):
        self.width = width
        self.height = height
        self.robots = parse(inp)
    def move(self, seconds):
        for i in range(len(self.robots)):
            px = (self.robots[i].px + self.robots[i].vx * seconds) % self.width
            py = (self.robots[i].py + self.robots[i].vy * seconds) % self.height
            self.robots[i] = Robot(px, py, self.robots[i].vx, self.robots[i].vy)
        return self
    def counts(self):
        counts = [([0]*self.width)[:] for _ in range(self.height)]
        for r in self.robots:
            counts[r.py][r.px] += 1
        return counts
    def __str__(self):
        #counts = []
        #for row in range(self.height):
        #    counts.append([0] * self.width)
        #for r in self.robots:
        #    counts[r.py][r.px] += 1
        #return '\n'.join(''.join(str(x) if x > 0 else '.' for x in line) for line in counts)
        return '\n'.join(''.join(str(x) if x > 0 else '.' for x in line) for line in self.counts())
    def quadrants(self):
        qq = [0,0,0,0]
        mid_height = self.height // 2
        mid_width = self.width // 2
        for r in self.robots:
            if r.px == mid_width or r.py == mid_height:
                continue
            q = 2 * int(r.px < mid_width) + int(r.py < mid_height)
            qq[q] += 1
        return qq
    def safety_factor(self):
        sf = 1
        for q in self.quadrants():
            sf *= q
        return sf

assert (got := Grid(11, 7, example_input).move(100).quadrants()) == [1, 3, 4, 1], got
assert (got := Grid(11, 7, example_input).move(100).safety_factor()) == 12, got

print(Grid(101, 103, open('inputs/day14.input.txt').read()).move(100).safety_factor())
