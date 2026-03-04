import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])
arr.sort(key=lambda i: (i[1], i[0]))
for i in arr:
    print(*i)