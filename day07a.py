#!/usr/bin/env python3

example_input = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def attempt(goal, numbers, acc=None, path=""):
    if not numbers:
        if acc == goal:
            yield path
        return
    elif not acc:
        n = numbers[0]
        yield from attempt(goal, numbers[1:], n, str(n))
    elif acc > goal:
        return
    else:
        n = numbers[0]
        yield from attempt(goal, numbers[1:], acc + n, path+f" + {n}")
        yield from attempt(goal, numbers[1:], acc * n, path+f" * {n}")

def possible(s):
    l, r = s.split(": ")
    for expr in attempt(int(l), [int(n) for n in r.split()]):
        return int(l)
    return 0

def run(inp):
    return sum((possible(line) for line in inp.splitlines()))

assert (got := run(example_input)) == 3749, got

print(run(open("inputs/day07.input.txt").read()))
