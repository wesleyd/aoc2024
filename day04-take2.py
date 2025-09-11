#!/usr/bin/env python3

example_input = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

class Grid():
    def __init__(self, inp):
        self.grid = inp.splitlines()
    def width(self):
        return len(self.grid[0])
    def height(self):
        return len(self.grid)
    def at(self, row, col):
        if row < 0 or self.width() <= row or col < 0 or self.height() <= col:
            return ''
        return self.grid[row][col]
    def line(self, row, col, drow, dcol):
        ret = ''
        for i in range(4):
            ret += self.at(row,col)
            row += drow
            col += dcol
        return ret
    def star(self, row, col):
        yield self.line(row, col,  0, +1)
        yield self.line(row, col, +1, +1)
        yield self.line(row, col, +1,  0)
        yield self.line(row, col, +1, -1)
        yield self.line(row, col,  0, -1)
        yield self.line(row, col, -1, -1)
        yield self.line(row, col, -1,  0)
        yield self.line(row, col, -1, +1)
    def xmases(self):
        n = 0
        for row in range(self.height()):
            for col in range(self.width()):
                n += list(self.star(row, col)).count('XMAS')
        return n

assert (got := Grid(example_input).xmases()) == 18, got

print(Grid(open('inputs/day04.input.txt').read()).xmases())

### 

class Grid2(Grid):
    def mas(self, row, col):
        a = self.at(row-1,col-1) + self.at(row,col) + self.at(row+1,col+1)
        b = self.at(row+1,col-1) + self.at(row,col) + self.at(row-1,col+1)
        return a in ('MAS', 'SAM') and b in ('MAS', 'SAM')
    def masses(self):
        n = 0
        for row in range(self.height()):
            for col in range(self.width()):
                if self.mas(row, col):
                    n+=1
        return n
assert (got := Grid2(example_input).masses()) == 9, got

print(Grid2(open('inputs/day04.input.txt').read()).masses())
