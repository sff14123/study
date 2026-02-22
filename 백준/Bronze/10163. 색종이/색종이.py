n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for a in range(n):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = a + 1
for a in range(n):
    cnt = 0
    for r in arr:
        for c in r:
            if c == a + 1:
                cnt += 1
    print(cnt)