import sys
from collections import deque

"""
Usage

> python3 queens2.py 13 10 10
> python3 queens2.py 8

"""


SIZE = int(sys.argv[1])


def i2q(i, size):
    ret = ""
    while i:
        ret += {0: " ", 1: ".", 3: "Q"}[i & 3]
        i >>= 2
    return ret.ljust(size)


def p(board, size, prefix=""):
    print(f"{prefix}+" + "-" * size + "+")
    print("\n".join(f"{prefix}|" + i2q(x, size) + "|" for x in board))
    print(f"{prefix}+" + "-" * size + "+")


# @profile
def q(board, x, y, size):
    #    print((x, y))
    for i in range(size):
        board[y] |= 1 << (i << 1)

    i = 0
    while True:
        try:
            board[i] |= 1 << (x << 1)
            i += 1
        except IndexError:
            break

    i = 0
    while True:
        if y - i < 0 or x + i >= size:
            break
        board[y - i] |= 1 << ((x + i) << 1)
        i += 1

    i = 0
    while True:
        try:
            if x - i < 0:
                break
            board[y + i] |= 1 << ((x - i) << 1)
            i += 1
        except IndexError:
            break
    i = 0
    while True:
        try:
            if x + i >= size:
                break
            board[y + i] |= 1 << ((x + i) << 1)
            i += 1
        except IndexError:
            break
    i = 0
    while True:
        try:
            if y - i < 0 or x - i < 0:
                break
            board[y - i] |= 1 << ((x - i) << 1)
            i += 1
        except IndexError:
            break

    board[y] |= 3 << (x << 1)


# @profile
def w(b, size):
    ret = []
    for i, c in enumerate(b):
        mask = 3
        for j in range(size):
            if c & mask == 0:
                ret.append((j, i))
            mask <<= 2
        if ret:
            break
    return ret


# @profile
def main(qx, qy, size):
    stack = deque()
    board = [0] * size
    q(board, qx, qy, size)
    # State = (board, # queens on the board,  list of moves (x,y) )
    stack.append((board, 1, w(board, size)))
    while stack:
        board, nq, moves = stack[-1]
        if nq == size:
            return board
        if moves:
            x, y = moves.pop(0)
            board_copy = list(board)
            q(board_copy, x, y, size)
            stack.append((board_copy, nq + 1, w(board_copy, size)))
        else:
            # print("DEAD END!")
            stack.pop()


assert (main(4, 5, 8)) == [21853, 30037, 21877, 23893, 54613, 22357, 21847, 21973]
x = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y = int(sys.argv[3]) if len(sys.argv) > 3 else 0
b = main(x, y, SIZE)
if b:
    p(b, SIZE)
else:
    print("No solution")
