#!/usr/bin/env python3

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

class Grid:
    def __init__(self, inp):
        pieces = inp.split('\n\n')
        self.grid = [list(line) for line in pieces[0].splitlines()]
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.moves = list(pieces[1].replace('\n',''))
        self.moves.reverse()
        self.robot = self._find_robot()
    def _find_robot(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == '@':
                    return (row, col)
    def __str__(self):
        return '\n'.join(''.join(s) for s in self.grid) + ''.join(self.moves[::-1])

def move1(g, dirn):
    row, col = g.robot
    assert g.grid[row][col] == '@'
    drow, dcol = 0, 0
    if dirn == '>':
        dcol = 1
    elif dirn == '<':
        dcol = -1
    elif dirn == '^':
        drow = -1
    elif dirn == 'v':
        drow = +1
    row2 = row + drow
    col2 = col + dcol
    if g.grid[row2][col2] == '#':
        return
    elif g.grid[row2][col2] == '.':
        g.grid[row][col] = '.'
        g.grid[row2][col2] = '@'
        g.robot = (row2, col2)
        return
    assert (ch := g.grid[row2][col2]) == 'O', f'ch={ch} != O at ({row2},{col2})'
    row3 = row2
    col3 = col2
    while g.grid[row3][col3] == 'O':
        row3 += drow
        col3 += dcol
    if g.grid[row3][col3] == '#':
        return
    assert (ch := g.grid[row3][col3]) == '.',  f'ch={ch} != . at ({row3},{col3})'
    g.grid[row][col] = '.'
    g.robot = (row2, col2)
    g.grid[row2][col2] = '@'
    g.grid[row3][col3] = 'O'

def play(g):
    while g.moves:
        dirn = g.moves.pop()
        move1(g, dirn)
    return g

def gps(g):
    n = 0
    for row in range(g.height):
        for col in range(g.width):
            if g.grid[row][col] == 'O':
                n += 100*row + col
    return n

assert (got := gps(Grid("""\
#######
#@..O..
#......

<
"""))) == 104, got

assert (got := str(play(Grid(example_input_1)))) == """\
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""", got
assert (got := gps(play(Grid(example_input_1)))) == 2028, got

assert (got := str(play(Grid(example_input_2)))) == """\
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########""",got
assert (got := gps(play(Grid(example_input_2)))) == 10092, got

print(gps(play(Grid(open('inputs/day15.input.txt').read()))))
