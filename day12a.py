#!/usr/bin/env python3

class Farm:
    def __init__(self, inp):
        self.grid = inp.splitlines()
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.plots = {}
        for row in range(self.height):
            for col in range(self.width):
                self.plots[(row, col)] = self.grid[row][col]
    def neighbors(self, plot):
        row, col = plot
        for drow, dcol in ((-1,0), (+1, 0), (0, -1), (0, +1)):
            row2 = row + drow
            col2 = col + dcol
            if 0 <= row2 and row2 < self.height and 0 <= col2 and col2 < self.height:
                yield (row2, col2)
    def regionize(self):
        regions = []
        plots = self.plots.copy()
        while plots:
            plot, crop = plots.popitem()
            inside = set()
            outside = set()
            candidates = set([plot])
            while candidates:
                p = candidates.pop()
                if p in inside or p in outside:
                    continue
                if self.plots[p] == crop:
                    inside.add(p)
                    plots.pop(p, None)
                    for neigh in self.neighbors(p):
                        if neigh in candidates or neigh in inside or neigh in outside:
                            continue
                        candidates.add(neigh)
                else:
                    outside.add(p)
            regions.append(inside)
        return regions

example_input_1 = """\
AAAA
BBCD
BBCC
EEEC
"""
example_input_2 = """\
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

example_input_3 = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

#print(Farm(example_input_1).regionize())

def area(region):
    return len(region)

def perimeter(region):
    perim = 0
    for p in region:
        row, col = p
        for drow, dcol in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            row2 = row + drow
            col2 = col + dcol
            p2 = (row2, col2)
            if p2 not in region:
                perim += 1
    return perim

def price(farm):
    return sum(area(r) * perimeter(r) for r in farm.regionize())

assert (got := price(Farm(example_input_1))) == 140, got
assert (got := price(Farm(example_input_2))) == 772, got
assert (got := price(Farm(example_input_3))) == 1930, got

print(price(Farm(open('inputs/day12.input.txt').read())))
