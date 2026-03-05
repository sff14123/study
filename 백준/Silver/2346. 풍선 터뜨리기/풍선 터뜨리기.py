import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    balloons = deque(enumerate(map(int, input().split()), start=1))

    results = []

    while balloons:
        idx, move = balloons.popleft()
        results.append(str(idx))

        if not balloons:
            break

        if move > 0:
            balloons.rotate(-(move - 1))
        else:
            balloons.rotate(-move)

    print(" ".join(results))

solve()