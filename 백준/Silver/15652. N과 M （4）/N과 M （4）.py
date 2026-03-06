import sys
input = lambda : sys.stdin.readline()

n, m = map(int, input().split())
result = []

def solve(start, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return

    for i in range(start, n + 1):
        result.append(i)
        solve(i, depth + 1) 
        result.pop()

solve(1, 0)