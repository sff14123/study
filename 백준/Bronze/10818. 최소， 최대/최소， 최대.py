import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# arr.sort()
# print(arr[0], arr[-1])
min_v = 1000000
max_v = -1000000
for r in arr:
    if min_v > r:
        min_v = r
    if max_v < r:
        max_v = r
print(min_v, max_v)