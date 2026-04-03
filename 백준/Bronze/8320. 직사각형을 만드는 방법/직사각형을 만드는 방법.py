import sys

n = int(sys.stdin.readline())
cnt = 0
for a in range(1, int(n**0.5) + 1):
    cnt += (n // a) - a + 1

print(cnt)