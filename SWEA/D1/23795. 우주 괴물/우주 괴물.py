T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    monster = ()
    d = [[-1,0], [1, 0], [0, -1], [0, 1]]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                monster = i, j
    i, j = monster
    for r in range(4):
        ni, nj = i + d[r][0], j + d[r][1]
        while 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 0:
                arr[ni][nj] = -1
            else:
                break
            ni += d[r][0]
            nj += d[r][1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc} {cnt}')