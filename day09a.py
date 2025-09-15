#!/usr/bin/env python3

example_input1 = "12345"

class Block:
    def __init__(self, file_id, length):
        self.file_id = file_id
        self.length = length
        self.prv = None
        self.nxt = None
    def is_space(self):
        return self.file_id == -1

def parse(inp):
    "parse turns inp into a doubly linked list of Block's."""
    blocks = []
    is_data = True
    file_id = 0
    for c in inp:
        length = int(c)
        if is_data:
            blocks.append(Block(file_id, length))
            file_id += 1
            is_data = False
        else:
            blocks.append(Block(-1, length))  # Space
            is_data = True
    head = blocks[0]
    tail = head
    for i in range(1, len(blocks)):
        block = blocks[i]
        tail.nxt = block
        block.prv = tail
        tail = block
    return head

def render(head):
    """render draws head block by block."""
    ret = []
    while head.prv:
        head = head.prv
    block = head
    while block:
        if block.is_space():
            c = '.'
        else:
            c = str(block.file_id)
        ret.append(c * block.length)
        block = block.nxt
    return ''.join(ret)

assert (got := render(parse('12345'))) == '0..111....22222', got
assert (got := render(parse('2333133121414131402'))) == '00...111...2...333.44.5555.6666.777.888899', got

def compress(head):
    orig_head = head
    tail = head
    while tail.nxt:
        tail = tail.nxt
    while head != tail:
        if not head.is_space():
            head = head.nxt
        elif tail.is_space() or tail.length == 0:
            tail = tail.prv
            tail.nxt = None
        elif tail.length >= head.length:
            head.file_id = tail.file_id
            tail.length -= head.length
            head = head.nxt
        else:  # tail.length < head.length
            head.length -= tail.length
            block = tail
            tail = tail.prv
            tail.nxt = None
            head.prv.nxt = block
            block.prv = head.prv
            block.nxt = head
            head.prv = block
    while tail.is_space():
        tail.prv.nxt = None
        tail = tail.prv
    return orig_head

assert (got := render(compress(parse('12345')))) == '022111222', got
assert (got := render(compress(parse('2333133121414131402')))) == '0099811188827773336446555566', got

def checksum(head):
    cs = 0
    pos = 0
    p = head
    while p:
        if p.is_space():
            continue
        for i in range(p.length):
            cs += pos * p.file_id
            pos += 1
        p = p.nxt
    return cs

assert (got := checksum(compress(parse('2333133121414131402')))) == 1928, got

print(checksum(compress(parse(open('inputs/day09.input.txt').read().strip()))))
