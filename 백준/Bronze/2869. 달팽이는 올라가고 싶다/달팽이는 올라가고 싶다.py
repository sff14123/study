import sys
a, b, v = map(int, sys.stdin.readline().split())
end = v - a
cnt = end // (a - b) + 1
if end % (a - b) != 0:
    cnt += 1
print(cnt)