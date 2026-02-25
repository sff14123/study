import sys

n, m = map(int, sys.stdin.readline().split())
arr = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]
print(*arr)
