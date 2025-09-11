#!/usr/bin/env python3

from collections import defaultdict
from functools import cmp_to_key

example_input = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

class Sorter:
    def __init__(self, inp):
        self.orders = set()
        for line in inp.splitlines():
            l, r = line.split("|")
            self.orders.add((int(l),int(r)))
    def __repr__(self):
        return f"Sorter({self.orders})"
    def sort(self, book):
        modified = False
        for i in range(len(book)-1):
            for j in range(i+1, len(book)):
                if (book[j],book[i]) in self.orders:
                    book[i], book[j] = book[j], book[i]
                    modified = True
        return modified

def parse(inp):
    a, b = inp.split("\n\n")
    books = []
    for line in b.splitlines():
        books.append([int(n) for n in line.split(",")])
    return Sorter(a), books

def run(inp):
    sorter, books = parse(inp)
    middle_totals = 0
    for book in books:
        if sorter.sort(book):
            middle = book[len(book)//2]
            middle_totals += middle
    return middle_totals

assert (got := run(example_input)) == 123, got

print(run(open('inputs/day05.input.txt').read()))
