import sys
n = int(sys.stdin.readline())
arr = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(n):
    y, x = map(int, sys.stdin.readline().split())
    y -= 1; x -= 1
    for i in range(y, y+10):
        for j in range(x, x+10):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)