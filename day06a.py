#!/usr/bin/env python3

example_input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

class Maze:
    def __init__(self, inp):
        self.obstacles = set()
        row = 0
        for line in inp.splitlines():
            col = 0
            for c in line:
                if c == '#':
                    self.obstacles.add((row, col))
                elif c == '^':
                    self.at = (row, col)
                    self.direction = 'UP'
                col += 1
            row += 1
        self.height = row
        self.width = col
        self.visited = set()
    def move1(self):
        self.visited.add(self.at)
        row, col = self.at
        if self.direction == 'UP':
            row -= 1
        elif self.direction == 'RIGHT':
            col += 1
        elif self.direction == 'DOWN':
            row += 1
        elif self.direction == 'LEFT':
            col -= 1
        if (row, col) in self.obstacles:
            if self.direction == 'UP':
                self.direction = 'RIGHT'
            elif self.direction == 'RIGHT':
                self.direction = 'DOWN'
            elif self.direction == 'DOWN':
                self.direction = 'LEFT'
            elif self.direction == 'LEFT':
                self.direction = 'UP'
        else:
            self.at = (row, col)
    def out_of_bounds(self):
        row, col = self.at
        return row < 0 or row >= self.height or col < 0 or col >= self.height
    def move(self):
        while not self.out_of_bounds():
            self.move1()
        return len(self.visited)

assert (got := Maze(example_input).move()) == 41, got

print(Maze(open('inputs/day06.input.txt').read()).move())
