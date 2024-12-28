#!/usr/bin/env python3

test_input = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip().splitlines()

def lookup1(inp, row, col):
    if row < 0 or len(inp) <= row:
        return '.'
    if col < 0 or len(inp[row]) <= col:
        return '.'
    return inp[row][col]

def xmas_at(inp, row, col):
    A = lookup1(inp, row, col) 
    ms1 = lookup1(inp, row-1, col+1) + A + lookup1(inp, row+1, col-1)
    ms2 = lookup1(inp, row-1, col-1) + A + lookup1(inp, row+1, col+1)
    both = ['MAS', 'SAM']
    return ms1 in both and ms2 in both

def run(inp):
    nxmas = 0
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if xmas_at(inp, row, col):
                nxmas += 1
    return nxmas

assert (got := run(test_input)) == 9, got

real_input = open('inputs/day04.input.txt').read().strip().splitlines()
print(run(real_input)) # => 1905
