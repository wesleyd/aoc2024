#!/usr/bin/env python3

def parse(inp):
    return inp.splitlines()
def height(grid):
    return len(grid)
def width(grid):
    return len(grid[0])

def origins(grid):
    for row in range(height(grid)):
        for col in range(width(grid)):
            if grid[row][col] == '0':
                yield (row,col)

example_input_1 = """\
0123
1234
8765
9876
"""
assert (got := list(origins(parse(example_input_1)))) == [(0,0)], got

example_input_2 = """\
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""
assert (got := list(origins(parse(example_input_2)))) == [(0,3)], got

example_input_3 = """\
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
"""
assert (got := list(origins(parse(example_input_3)))) == [(0,1), (6,5)], got

example_input_4 = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
assert (got := list(origins(parse(example_input_4)))) == [(0,2), (0,4), (2,4), (4,6), (5,2), (5,5), (6,0), (6,6), (7,1)], got

def nexts(grid, row, col):
    nxt = str(int(grid[row][col]) + 1)
    for (drow, dcol) in ((-1,0), (+1, 0), (0,-1), (0,+1)):
            c = col+dcol
            r = row+drow
            if 0 <= c and c < width(grid) and 0 <= r and r < height(grid) and grid[r][c] == nxt:
                yield (r,c)

def explore(grid, row, col, path=None):
    if not path:
        path = []
    else:
        path = path[:]
    path.append((row,col))
    if grid[row][col] == '9':
        yield path
    else:
        for r, c in nexts(grid, row, col):
            yield from explore(grid, r, c, path)

def rating(grid):
    r = 0
    st = set()
    for r0, c0 in origins(grid):
        for path in explore(grid, r0, c0):
            st.add(tuple(path))
    return len(st)

example_input_5 = """\
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
"""
assert (got :=rating(parse(example_input_5))) == 3, got

example_input_6 = """\
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""
assert (got :=rating(parse(example_input_6))) == 13, got

example_input_7 = """\
012345
123456
234567
345678
4.6789
56789.
"""
assert (got :=rating(parse(example_input_7))) == 227, got

assert (got :=rating(parse(example_input_4))) == 81, got

print(rating(parse(open('inputs/day10.input.txt').read())))
