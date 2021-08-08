import sys
from collections import deque
from multiprocessing import Process, Queue

"""
Usage

> python3 queens4.py 13 10 10
> python3 queens4.py 8

"""


SIZE = int(sys.argv[1])


def p(q, size, prefix=""):
    board = [["."] * size for _ in range(size)]
    for x, y in q:
        board[y][x] = "Q"
    print(f"{prefix}+" + "-" * size + "+")
    print("\n".join(f"{prefix}|" + ("".join(x)) + "|" for x in board))
    print(f"{prefix}+" + "-" * size + "+")


# @profile
def q(queens, board_free, x, y, size):
    #    print((x, y))
    for i in range(size):
        board_free.discard((i, y))
        board_free.discard((x, i))
        board_free.discard((x + i, y + i))
        board_free.discard((x - i, y - i))
        board_free.discard((x + i, y - i))
        board_free.discard((x - i, y + i))
    board_free.discard((x, y))
    queens.add((x, y))


def process(queens, board_free, size, out_queue):
    stack = deque()
    stack.append((queens, board_free))
    while stack:
        queens, board_free = stack[-1]
        if len(queens) == size:
            out_queue.put(queens)
            return
        if board_free:
            x, y = board_free.pop()
            queens_copy = set(queens)
            board_free_copy = set(board_free)
            q(queens_copy, board_free_copy, x, y, size)
            stack.append((queens_copy, board_free_copy))
        else:
            # print("DEAD END!")
            stack.pop()
    out_queue.put(None)


# @profile
def main(qx, qy, size):
    board_free = set((x, y) for x in range(size) for y in range(size))
    queens = set()
    q(queens, board_free, qx, qy, size)
    queue = Queue()
    pro = []
    first_row = 0 if qy != 0 else 1
    for move in ((x, y) for x, y in board_free if y == first_row):
        queens_copy = set(queens)
        board_free_copy = set(board_free)
        q(queens_copy, board_free_copy, move[0], move[1], size)
        proc = Process(target=process, args=(queens_copy, board_free_copy, size, queue))
        pro.append(proc)
        proc.start()
    rets = 0
    while rets < len(pro):
        ret = queue.get()
        rets += 1
        if ret is not None:
            [p.terminate() for p in pro]
            return ret


p(main(4, 5, 8), 8)
assert main(4, 5, 8) == {(7, 3), (3, 0), (0, 6), (2, 2), (4, 5), (6, 1), (5, 7), (1, 4)}
x = int(sys.argv[2]) if len(sys.argv) > 2 else 0
y = int(sys.argv[3]) if len(sys.argv) > 3 else 0
b = main(x, y, SIZE)
if b:
    p(b, SIZE)
else:
    print("No solution")
