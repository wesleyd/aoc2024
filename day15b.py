#!/usr/bin/env python3

import copy

example_input_1 = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

example_input_2 = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

example_input_3 = """\
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

class Grid:
    def __init__(self, inp):
        pieces = inp.split('\n\n')
        self.grid = []
        for line in pieces[0].splitlines():
            l = []
            for c in line:
                if c == 'O':
                    l.extend('[]')
                elif c == '#':
                    l.extend('##')
                elif c == '.':
                    l.extend('..')
                elif c == '@':
                    l.extend('@.')
                else:
                    assert False, f'bad character {c}'
            self.grid.append(l)
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.moves = list(pieces[1].replace('\n',''))
        self.moves.reverse()
        self.robot = self._find_robot()
        self.nboxes = self.count_boxes()
    def _find_robot(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == '@':
                    return (row, col)
    def count_boxes(self):
        n = 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == '[':
                    n += 1
        return n
    def __str__(self):
        #return '\n'.join(''.join(s) for s in self.grid) + ''.join(self.moves[::-1])
        return '\n'.join(''.join(s) for s in self.grid) + '\n' + ''.join(self.moves[-1:])

def move_left_right(g, dirn):
    row, col = g.robot
    dcol = 0
    if dirn == '<':
        dcol = -1
    elif dirn == '>':
        dcol = +1
    else:
        assert False, f'bad LR direction {dirn}'
    col2 = col
    while g.grid[row][col2] in '@[]':
        col2 += dcol
    if g.grid[row][col2] != '.':
        return
    while col2 != col:
        g.grid[row][col2] = g.grid[row][col2-dcol]
        col2 -= dcol
    g.grid[row][col] = '.'
    g.robot = row, col+dcol

class HitWall(Exception):
    pass

def push_up_down(grid, row, col, drow):
    if grid[row][col] == '#':
        raise HitWall
    elif grid[row][col] == '.':
        return
    elif grid[row][col] == '@':
        push_up_down(grid, row+drow, col, drow)
        grid[row+drow][col] = grid[row][col]
        grid[row][col] = '.'
    elif grid[row][col] == ']':
        push_up_down(grid, row+drow, col-1, drow)
        push_up_down(grid, row+drow, col, drow)
        grid[row+drow][col-1] = grid[row][col-1]
        grid[row+drow][col] = grid[row][col]
        grid[row][col-1] = '.'
        grid[row][col] = '.'
    elif grid[row][col] == '[':
        push_up_down(grid, row+drow, col, drow)
        push_up_down(grid, row+drow, col+1, drow)
        grid[row+drow][col] = grid[row][col]
        grid[row+drow][col+1] = grid[row][col+1]
        grid[row][col] = '.'
        grid[row][col+1] = '.'

def move_up_down(g, dirn):
    row, col = g.robot
    drow = 0
    if dirn == '^':
        drow = -1
    elif dirn == 'v':
        drow = +1
    grid = copy.deepcopy(g.grid)
    try:
        push_up_down(grid, row, col, drow)
    except HitWall:
        return
    g.grid = grid
    g.robot = g._find_robot()

def move1(g, dirn):
    if dirn in '<>':
        move_left_right(g, dirn)
    elif dirn in 'v^':
        move_up_down(g, dirn)
    else:
        assert False, f'bad direction {dirn}'

def play(g):
    while g.moves:
        dirn = g.moves.pop()
        move1(g, dirn)
    return g

assert (got := str(play(Grid(example_input_3)))) == """\
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
"""

def gps(g):
    i = 0
    n = 0
    for row in range(g.height):
        for col in range(g.width):
            if g.grid[row][col] == '[':
                n += 100*row + col
    return n

eg = Grid(example_input_2)
play(eg)
assert (got := str(eg)) == """\
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
"""
assert (got := gps(eg)) == 9021, got

print(gps(play(Grid(open('inputs/day15.input.txt').read()))))
