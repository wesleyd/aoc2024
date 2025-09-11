#!/usr/bin/env python3

from collections import defaultdict
from itertools import permutations

example_input1 = """\
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
"""

example_input2 = """\
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
"""

class Grid:
    def __init__(self, inp):
        grid = inp.splitlines()
        self.height = len(grid)
        self.width = len(grid[0])
        self.antennas = defaultdict(set)
        for row in range(self.height):
            for col in range(self.width):
                if (c := grid[row][col]) not in ('.', '#'):
                    self.antennas[c].add((row, col))
    def antinodes(self):
        ret = set()
        for freq, antennas in self.antennas.items():
            for a, b in permutations(antennas, 2):
                row, col = a[0], a[1]
                drow = a[0] - b[0]
                dcol = a[1] - b[1]
                while 0 <= row and row < self.height and 0 <= col and col < self.width:
                    ret.add((row, col))
                    row += drow
                    col += dcol
        return ret

assert (got := len(Grid(example_input1).antinodes())) == 34, got
assert (got := len(Grid(example_input2).antinodes())) == 9, got

print(len(Grid(open('inputs/day08.input.txt').read()).antinodes()))
