import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
def solve(start, depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n + 1):
        result.append(i)
        solve(i + 1, depth + 1)
        result.pop()
result = []
solve(1, 0)