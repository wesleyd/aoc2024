#!/usr/bin/env python3

from copy import deepcopy

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
                    self.start = (row, col)
                    self.direction = 'UP'
                col += 1
            row += 1
        self.height = row
        self.width = col

class Walker:
    def __init__(self, maze, extra_obstacle=None):
        self.at = maze.start
        self.direction = 'UP'
        self.visited = set()
        self.obstacles = maze.obstacles.copy()
        if extra_obstacle:
            self.obstacles.add(extra_obstacle)
            #print(self.obstacles)
        self.maze = maze
    def mark(self):
        self.visited.add((self.direction, self.at))
    def looped(self):
        return (self.direction, self.at) in self.visited
    def move1(self):
        self.mark()
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
        return row < 0 or row >= self.maze.height or col < 0 or col >= self.maze.height
    def move(self):
        while not self.out_of_bounds() and not self.looped():
            self.move1()

def try_obstacle(maze, obstacle):
    "Returns True if obstacle would cause a loop."
    w = Walker(maze, obstacle)
    w.move()
    return w.looped()

def place_obstacles(maze):
    w = Walker(maze)
    w.move()
    assert not w.looped(), "Empty maze looped!"
    # Only need to place obstacles in places guard will visit...
    locations = set()
    for _, p in w.visited:
        if p == maze.start:
            # Can't place an obstacle at guard start!
            continue
        locations.add(p)
    n = 0
    for ob in locations:
        if try_obstacle(maze, ob):
            n += 1
    return n

assert (got := place_obstacles(Maze(example_input))) == 6, got

print(place_obstacles(Maze(open('inputs/day06.input.txt').read())))
