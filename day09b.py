#!/usr/bin/env python3

example_input1 = "12345"

class Block:
    def __init__(self, file_id, length):
        self.file_id = file_id
        self.length = length
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
        tail = block
    return head

def render(head):
    """render draws head block by block."""
    ret = []
    while head:
        if head.is_space():
            c = '.'
        else:
            c = str(head.file_id)
        ret.append(c * head.length)
        head = head.nxt
    return ''.join(ret)
assert (got := render(parse('12345'))) == '0..111....22222', got
assert (got := render(parse('2333133121414131402'))) == '00...111...2...333.44.5555.6666.777.888899', got

def find_max_file_id(head):
    max_file_id = -1
    while head:
        if head.file_id > max_file_id:
            max_file_id = head.file_id
        head = head.nxt
    return max_file_id

def compress1(head, file_id):
    src = head
    while src:
        if src.file_id == file_id:
            break
        src = src.nxt
    assert src, f"no such file_id {file_id}"
    dst = head
    while dst and dst != src:
        if dst.is_space():
            if dst.length >= src.length:
                break
        dst = dst.nxt
    else:
        # print(f"can't move file_id {file_id} left, no contiguous space ({src.length})")
        return
    assert dst.is_space(), "dst is not space!"
    leftover = dst.length - src.length
    dst.file_id = src.file_id
    dst.length = src.length
    if leftover > 0:
        extra = Block(-1, leftover)
        extra.nxt = dst.nxt
        dst.nxt = extra
    src.file_id = -1
    p = head
    while p and p.nxt:
        if p.file_id == p.nxt.file_id:
            p.length += p.nxt.length
            p.nxt = p.nxt.nxt
        else:
            p = p.nxt

def compress(head):
    max_file_id = find_max_file_id(head)
    for file_id in range(max_file_id, -1, -1):
        compress1(head, file_id)
    return head

assert (got := render(compress(parse('2333133121414131402')))) == '00992111777.44.333....5555.6666.....8888..', got

def checksum(head):
    cs = 0
    pos = 0
    while head:
        if not head.is_space():
            for i in range(head.length):
                cs += pos * head.file_id
                pos += 1
        else:
            pos += head.length
        head = head.nxt
    return cs

assert (got := checksum(compress(parse('2333133121414131402')))) == 2858, got

print(checksum(compress(parse(open('inputs/day09.input.txt').read().strip()))))
