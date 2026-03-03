import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0
        start = 'W'

        for r in range(8):
            current = start
            for c in range(8):
                if arr[i+r][j+c] != current:
                    cnt += 1
                current = 'B' if current == 'W' else 'W'
            start = 'B' if start == 'W' else 'W'
        ans = min(ans, cnt, 64 - cnt)
print(ans)