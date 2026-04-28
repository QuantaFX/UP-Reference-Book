import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

def next_int():
    return int(next(it))