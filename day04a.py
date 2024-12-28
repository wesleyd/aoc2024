#!/usr/bin/env python3

test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip().splitlines()

def lookup1(inp, row, col):
    if row < 0 or len(inp) <= row:
        return '.'
    if col < 0 or len(inp[row]) <= col:
        return '.'
    return inp[row][col]

def lookupDir(inp, row, col, drow, dcol):
    s = ''
    for i in range(4):
        s += lookup1(inp, row+i*drow, col+i*dcol)
    return s == 'XMAS'

def xmases(inp, row, col):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if lookupDir(inp, row, col, drow, dcol):
                yield row, col, drow, dcol

def run(inp):
    nxmas = 0
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            for xmas in xmases(inp, row, col):
                nxmas += 1
    return nxmas

assert (got := run(test_input)) == 18, got

real_input = open('inputs/day04.input.txt').read().strip().splitlines()
print(run(real_input)) # => 2613
