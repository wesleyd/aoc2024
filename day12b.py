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

def area(region):
    return len(region)

def sides(region):
    aboves = set()
    belows = set()
    lefts = set()
    rights = set()
    for p in region:
        row, col = p
        if (row-1, col) not in region:
            aboves.add(p)
        if (row+1, col) not in region:
            belows.add(p)
        if (row, col-1) not in region:
            lefts.add(p)
        if (row, col+1) not in region:
            rights.add(p)
    return ( count_horizontals(aboves)
           + count_horizontals(belows)
           + count_verticals(lefts)
           + count_verticals(rights))

def count_horizontals(horizontals):
    horizontals = set(horizontals)
    nsides = 0
    while horizontals:
        row, col = horizontals.pop()
        i = 1
        while (p := (row, col+i)) in horizontals:
            horizontals.remove(p)
            i += 1
        i = 1
        while (p := (row, col-i)) in horizontals:
            horizontals.remove(p)
            i += 1
        nsides += 1
    return nsides

def count_verticals(verticals):
    return count_horizontals(set((c, r) for (r, c) in verticals))

def price(farm):
    return sum(area(r) * sides(r) for r in farm.regionize())

assert (got := price(Farm(example_input_1))) == 80, got
assert (got := price(Farm(example_input_2))) == 436, got
assert (got := price(Farm(example_input_3))) == 1206, got

example_input_4 = """\
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""
assert (got := price(Farm(example_input_4))) == 236, got

example_input_5 = """\
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""
assert (got := price(Farm(example_input_5))) == 368, got

print(price(Farm(open('inputs/day12.input.txt').read())))
