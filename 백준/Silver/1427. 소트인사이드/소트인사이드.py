import sys
n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
print(*n, sep='')