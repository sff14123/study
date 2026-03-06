import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
def solve(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            solve(depth + 1)
            result.pop()
            visited[i] = False
visited = [False] * (n + 1)
result = []

solve(0)